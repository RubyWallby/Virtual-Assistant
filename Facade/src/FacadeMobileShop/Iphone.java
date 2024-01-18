package FacadeMobileShop;

public class Iphone implements IMobileShop {
    @Override
    public void modelNo() {
        System.out.println(" Iphone 6 ");
    }
    @Override
    public void price() {
        System.out.println(" Rs 65000.00 ");
    }
}