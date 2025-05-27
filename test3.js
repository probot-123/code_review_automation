// Account constructor function
function Account(accountName, country, businessName) {
  this.accountName = accountName;
  this.country = country;
  this.businessName = businessName;

  this.displayInfo = function () {
    console.log("Account Name:", this.accountName);
    console.log("Country:", this.country);
    console.log("Business Name:", this.businessName);
  };
}

// Create an instance of Account
const account = new Account("Yash Enterprises", "India", "Tech Solutions");

// Display account details
account.displayInfo();
