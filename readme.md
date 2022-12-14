Steps to generate Generic pass Via Google

1. Sign up for a Google Wallet API Issuer account: An Issuer account is necessary to create and distribute passes for Google Wallet.
 https://pay.google.com/business/console?utm_source=developers.google.com&utm_medium=referral link for Google Pay and Wallet Console to get your issuer account.
 While you wait for approval of your Issuer account, create a temporary developer account https://wallet-lab-tools.web.app/issuers?utm_source=developers.google.com&utm_medium=referral.

2. Enable the Wallet API: Sign into the Google Cloud Platform --> https://console.cloud.google.com/?utm_source=developers.google.com&utm_medium=referral ----> 
   and enable the Google Wallet API for your GCP(Google Cloud Platform) project. 
   If you don’t already have a GCP project, create one.
   Enable the Google Wallet API ---->  https://console.cloud.google.com/apis/library/walletobjects.googleapis.com?utm_source=developers.google.com&utm_medium=referral

3. Create a service account: A service account and a service account key are necessary to call the Google Wallet API. 
   The service account is the identity that calls the Google Wallet API. 
   The service account key contains a private key that identifies your application as the service account. 
   
   Create a service account: 1.Create a service account ---> https://console.cloud.google.com/iam-admin/serviceaccounts/create?utm_source=developers.google.com&utm_medium=referral in the Google Cloud Console, providing the following details:
                                    Service account name - example: Wallet Web Client
                                     Service account ID - example: my-service-account 
                             2. Click CREATE AND CONTINUE.  
                             3. Click DONE
   Create a service account key: 1. Select your service account. For example: my-service-account@my-project-id.iam.gserviceaccount.com.
                                 2. Click on the KEYS menu item at the top of the page.
                                 3. Click ADD KEY and Create new key.
                                 4. Select key type JSON.
                                 5. Click CREATE to create and download the service account key.

4. Authorize the service account: You must authorize the service account in order to call the API. 
     To authorize it, grant the service account access to manage your Issuer Account.
    Visit the Users page in the Google Pay and Wallet Console --> https://pay.google.com/business/console?utm_source=developers.google.com&utm_medium=referral.
             1. Click Invite a user.
             2. Add the service account's email address. For example: my-service-account@my-project-id.iam.gserviceaccount.com.
             3. Select Developer for Access level.
             4. Click Invite. 

5. Create a class :
    Before you can create and add a GenericObject, you must create a GenericClass. 
    This can be done using the Web API. For further information, please refer to the reference documentation --> https://developers.google.com/wallet/generic/rest/v1/genericclass for GenericClass, 
    as well as the getting started guide -->  https://developers.google.com/wallet/generic/web  for using the Web API.

