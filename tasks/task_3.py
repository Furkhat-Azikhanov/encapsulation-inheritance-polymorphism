# Есть абстрактный класс PaymentMethod с методом pay(amount).
# Реализуй несколько классов:
# CreditCard — печатает: "Оплата {amount} рублей картой."
# PayPal — печатает: "Оплата {amount} через PayPal."
# CryptoWallet — печатает: "Оплата {amount} в криптовалюте."

class PaymentMethod:
    def pay(self, amount: float):
        raise NotImplementedError("Метод должен быть реализован в подклассе.")


class CreditCard(PaymentMethod):
    def pay(self, amount: float):
        print(f"Оплата {amount} рублей картой.")


class PayPal(PaymentMethod):
    def pay(self, amount: float):
        print(f"Оплата {amount} через PayPal.")


class CryptoWallet(PaymentMethod):
    def pay(self, amount: float):
        print(f"Оплата {amount} в криптовалюте.")
        

def process_payment(method: PaymentMethod, amount: float):
    method.pay(amount)

