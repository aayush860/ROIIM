# ROIIM
paysafe

NOTE - (Frontend /checkout link may take time to load as i have little experience with frontend)

This application is using Django as backend-
with architecture

------------------------------------------------------------------------------------------------------------------------------------------------------------
ROIIM(Main APP)-
having 2 microservices-
1. signin - handeling registration and singin functionality
2. cart - handeling shopping window and checkout functionality, and providing little bit of support to customized callbacks

------------------------------------------------------------------------------------------------------------------------------------------------------------

Available urls-
1. signin-  to signin.
2. signup- to singup.
3. window- to add items in cart.
4. checkout-  handeling billing and payment functionalities.
5. payment_sucessuful- redirection on sucessful payment.
6. payment_unsucessuful- redirection on unsucessful payment.

------------------------------------------------------------------------------------------------------------------------------------------------------------
Database-
OnetoOne architecture is used to map user- 
-user(login functionality)
1. details_of_user_doing payment
2. billing_details_of_user_doing payment
        
NOTE-> There is one more table handeling api_key configuration in postgres database 
