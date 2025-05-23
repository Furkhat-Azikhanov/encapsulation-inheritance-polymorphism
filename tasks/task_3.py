# Есть абстрактный класс PaymentMethod с методом pay(amount).
# Реализуй несколько классов:
# CreditCard — печатает: "Оплата {amount} рублей картой."
# PayPal — печатает: "Оплата {amount} через PayPal."
# CryptoWallet — печатает: "Оплата {amount} в криптовалюте."
class PaymentMethod:
    def pay(self, amount: float):
        raise NotImplementedError("Метод должен быть реализован в подклассе.")


class CreditCard(PaymentMethod):
    pass


class PayPal(PaymentMethod):
    pass


class CryptoWallet(PaymentMethod):
    pass


def process_payment(method: PaymentMethod, amount: float):
    method.pay(amount)
