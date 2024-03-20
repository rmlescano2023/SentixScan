import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class Shoppee_Scrape {
    public static void main(String[] args) {
        
        WebDriver driver = new ChromeDriver(options);
        ChromeOptions options = new ChromeOptions();

        options.setExperimentalOption("detach", true);
        WebDriverWait wait = new WebDriverWait(driver, 10);

        String URL = "https://shopee.ph/XH-M609-12-36V-Low-Voltage-Battery-Disconnect-Protection-Module-DC-Output-i.951744141.22229984756?sp_atk=8a7df1e2-125b-4e14-b737-fe472bdcb8f6&xptdk=8a7df1e2-125b-4e14-b737-fe472bdcb8f6&is_from_login=true";
        driver.get(URL);

        try {
            wait.until(ExpectedConditions.visibilityOfElementLocated(By.className("K1dDgL")));
            System.out.println("Login page is visible");

            WebElement phone_number_input = driver.findElement(By.xpath("//input[@class='pDzPRp' and @type='text']"));
            phone_number_input.sendKeys("09455179798");

            WebElement password_input = driver.findElement(By.xpath("//input[@class='pDzPRp' and @type='password']"));
            password_input.sendKeys("your_password_here");

            /* WebElement login_button = driver.findElement(By.className("wyhvVD"));
            login_button.click(); */

        } catch (Exception e) {
            System.out.println("Login page is not visible");
            e.printStackTrace();
        }

        WebElement author_element = driver.findElement(By.xpath("//div[@class='product-ratings']//div[@class='product-ratings__list']//div[@class='shopee-product-comment-list']//div[@class='shopee-product-rating']//div[@class='shopee-product-rating__main']//a[@class='shopee-product-rating__author-name']"));
        WebElement review_element = driver.findElement(By.xpath("//div[@class='product-ratings']//div[@class='product-ratings__list']//div[@class='shopee-product-comment-list']//div[@class='shopee-product-rating']//div[@class='shopee-product-rating__main']"));

        String author_name = author_element.getText();
        String author_review = review_element.getText();

        System.out.println(author_name);
        System.out.println(author_review);

        WebElement next_button = driver.findElement(By.xpath("//button[@class='shopee-icon-button shopee-icon-button--right ']"));
        next_button.click();

        driver.quit();
    }
}
