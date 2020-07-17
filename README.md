# ROIIM
paysafe

NOTE - (Frontend /checkout link may take time to load as i have little experience with frontend)

This application is using Django as backend- (debug is on purpose kept true on deployment)
with architecture

------------------------------------------------------------------------------------------------------------------------------------------------------------
ROIIM(Main APP)-
having 2 microservices-
1. signin - handeling registration and singin functionality
2. cart - handeling shopping window and checkout functionality, and providing little bit of support to customized callbacks

------------------------------------------------------------------------------------------------------------------------------------------------------------

Available urls-
-> signin-  to signin
-> signup- to singup
-> window- to add items in cart
-> checkout-  handeling billing and payment functionalities
-> payment_sucessuful- redirection on sucessful payment
-> payment_unsucessuful- redirection on unsucessful payment

------------------------------------------------------------------------------------------------------------------------------------------------------------
Database-
OnetoOne architecture is used to map user- 
                                    user(login functionality)
                                     /\
                                    /  \
                                   /    \
                                  /      \
        details_of_user_doing payment    billing_details_of_user_doing payment
        
NOTE-> There is one more table handeling api_key configuration in postgres database 
