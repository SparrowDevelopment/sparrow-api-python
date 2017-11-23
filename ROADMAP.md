Current goal is to support as the whole [reference test suite][1].

[1]: https://github.com/SparrowDevelopment/sparrow-api-curl/blob/master/api


## [sale](tests/test_sale.py)

- [x] simple_sale
- [x] simple_sale_decline
- [x] simple_sale_invalid_card
- [x] simple_sale_avs_mismatch
- [x] advanced_sale
- [x] passenger_sale

## [auth](tests/test_auth.py)

- [x] simple_authorization
- [x] advanced_auth
- [x] simple_capture
- [x] simple_offline_capture
- [ ] :x: account_verification `Invalid amount REFID:xxxxxxxx` — see [#3]
- [ ] retrieve_card_balance

[#3]: https://github.com/SparrowDevelopment/sparrow-api-python/issues/3

## [refund](tests/test_refund.py)

- [x] simple_refund
- [x] advanced_refund
- [x] simple_void
- [x] advanced_void
- [x] chargeback_entry

## [ach](tests/test_ach.py)

- [x] simple_ach
- [x] simple_ach_refund
- [x] simple_ach_credit
- [x] advanced_ach

## [star](tests/test_star.py)

- [x] simple_star_card
- [x] advanced_star_card

## [ewallet](tests/test_ewallet.py)

- [x] e_wallet_simple_credit

## [fiserv](tests/test_fiserv.py)

- [x] fiserv_simple_sale
- [x] advanced_fiserv_sale

## [customers](tests/test_customers.py)

- [x] adding_a_customer
- [x] add_customer_credit_card_simple
- [x] add_customer_ach_simple
- [x] add_customer_e_wallet_simple
- [x] update_payment_type
- [x] delete_payment_type
- [x] delete_data_vault_customer
- [ ] :x: decrypting_custom_fields `Internal processing error` — see [sparrow-api-dotnet/notes.md]

[sparrow-api-dotnet/notes.md]: https://github.com/ricklove/sparrow-api-dotnet/blob/master/notes.md#decryptcustomfields

## [invoices](tests/test_invoices.py)

- [x] creating_an_invoice
- [x] creating_active_invoice
- [x] update_invoice
- [x] retrieve_invoice
- [x] cancel_invoice
- [x] cancel_invoice_by_customer
- [x] paying_an_invoice_with_a_credit_card
- [x] paying_an_invoice_with_a_bank_account

## [plans](tests/test_plans.py)

- [x] creating_a_payment_plan
- [x] updating_a_payment_plan
- [x] deleting_a_plan
- [x] assigning_a_payment_plan_to_a_customer
- [x] update_payment_plan_assignment
- [x] cancel_plan_assignment
