package FacadeMobileShop;

public class ShopKeeper
{
    private IMobileShop iphone;
    private IMobileShop samsung;
    private IMobileShop blackberry;

    public ShopKeeper(){
        iphone= new Iphone();
        samsung=new Samsung();
        blackberry=new Blackberry();
    }
    public void iphoneSale(){
        iphone.modelNo();
        iphone.price();
    }
    public void samsungSale(){
        samsung.modelNo();
        samsung.price();
    }
    public void blackberrySale(){
        blackberry.modelNo();
        blackberry.price();
    }
}