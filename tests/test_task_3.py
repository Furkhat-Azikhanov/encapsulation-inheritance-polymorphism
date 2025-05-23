import pytest
from tasks import CreditCard, PayPal, CryptoWallet, process_payment

def test_credit_card_payment(capfd):
    cc = CreditCard()
    process_payment(cc, 100)
    out, _ = capfd.readouterr()
    assert "Оплата 100 рублей картой." in out

def test_paypal_payment(capfd):
    pp = PayPal()
    process_payment(pp, 250.5)
    out, _ = capfd.readouterr()
    assert "Оплата 250.5 через PayPal." in out

def test_crypto_payment(capfd):
    crypto = CryptoWallet()
    process_payment(crypto, 777)
    out, _ = capfd.readouterr()
    assert "Оплата 777 в криптовалюте." in out
