public class Account {
    private String accountName;
    private String country;
    private String businessName;

    // Constructor
    public Account(String accountName, String country, String businessName) {
        this.accountName = accountName;
        this.country = country;
        this.businessName = businessName;
    }

    // Getters
    public String getAccountName() {
        return accountName;
    }

    public String getCountry() {
        return country;
    }

    public String getBusinessName() {
        return businessName;
    }

    // Display account details
    public void displayInfo() {
        System.out.println("Account Name: " + accountName);
        System.out.println("Country: " + country);
        System.out.println("Business Name: " + businessName);
    }

    // Main method to test the class
    public static void main(String[] args) {
        Account acc = new Account("Yash Enterprises", "India", "Tech Solutions");
        acc.displayInfo();
    }
}
