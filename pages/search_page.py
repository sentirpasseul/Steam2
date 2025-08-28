from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    SEARCH_SORT_BY = (By.XPATH, "//button[@*='sort_by_trigger']")
    SEARCH_SORT_BY_PRICE_DESC = (By.XPATH, "//a[@*='Price_DESC']")
    SEARCH_SORT_BY_PRICE_DESC_ACTIVE = (By.XPATH, "//input[@*='sort_by' and @value='Price_DESC']")
    SEARCH_RESULTS = (By.ID, "search_results")
    SEARCH_RESULT_ITEM_FINAL_PRICE = (By.XPATH, "//div[contains(@class,'discount_final_price')]")
    SEARCH_RESULT_ITEM_SALES_PRICE = (
        By.XPATH, "//div[contains(@class, 'discount_final_price your_price')]/div[2]")

    def get_all_prices(self):
        final_prices = self.find_all(self.SEARCH_RESULT_ITEM_FINAL_PRICE)
        sales_prices = self.find_all(self.SEARCH_RESULT_ITEM_SALES_PRICE)
        prices_data = []

        for i, final_price_element in enumerate(final_prices):
            try:
                final_price = final_price_element.text.strip()

                # Более безопасная проверка наличия скидочной цены
                has_sale = (i < len(sales_prices) and
                            sales_prices[i] and
                            bool(sales_prices[i].text.strip()))

                final_sale_price = sales_prices[i].text.strip() if has_sale else None

                prices_data.append({
                    'final_price': final_price,
                    'sale': has_sale,
                    'final_sale_price': final_sale_price
                })
            except Exception as e:
                print(f"Ошибка при получении цены элемента {i}: {e}")
                continue

        return [
            {
                'final_price': final_prices_element.text,
                'sale': i < len(sales_prices) and bool(sales_prices[i].text.strip()),
                'final_sale_price': sales_prices[i].text if i < len(sales_prices) and sales_prices[
                    i].text.strip() else None
            }
            for i, final_prices_element in enumerate(final_prices)
        ]

    def get_prices(self):
        all_prices = self.get_all_prices()
        return [
            item["final_sale_price"] if item["final_sale_price"] else
            item["final_price"]
            for item in all_prices[:10]
        ]
