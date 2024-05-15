let scrapeData = document.getElementById('scrapeData');

scrapeData.addEventListener("click", () => {
    // Get the current active tab in the Chrome window
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        if (tabs && tabs.length > 0) {
            const currentUrl = tabs[0].url;
            // alert("Current URL: " + currentUrl); // Display URL using alert
            extract_url(currentUrl);
        } else {
            console.error("Unable to retrieve current URL");
        }
    });
});


// Function to extract current URL
async function extract_url(currentUrl) {
    
    alert("Current URL: " + currentUrl);
    extract_ids(currentUrl);

}

async function extract_ids(currentUrl) {

    // alert("extract_ids function accessed");
    
    // Sample URL
    // const sampleUrl = "https://shopee.ph/Downy-Passion-Fabric-Conditioner-900-ml.-i.24817442.310022970"
    // const sampleUrl = "https://shopee.ph/Baseus-WM02-True-Wireless-Earphones-i.131196305.17552845260?sp_atk=9b052925-dc7d-4a16-af52-e5afa0b73fef&xptdk=9b052925-dc7d-4a16-af52-e5afa0b73fef"

    // RegEx expressions to extract shopId and itemId
    const shopIdPattern = /shopee.ph\/[^i]+[^.]+.(-i\.)?(?<shopId>[^.]+)/;
    const itemIdPattern = /shopee.ph\/[^i]+[^.]+.(-i\.)?[^.]+.(?<itemId>\d+)/;

    // Extracting shopId
    const shopIdMatch = currentUrl.match(shopIdPattern);
    const shopId = shopIdMatch ? shopIdMatch.groups.shopId : null;

    // Extracting itemId
    const itemIdMatch = currentUrl.match(itemIdPattern);
    const itemId = itemIdMatch ? itemIdMatch.groups.itemId : null;

    alert("Shop ID: " + shopId + "   Item ID: " + itemId);

    scrape_reviews(shopId, itemId);
}

async function scrape_reviews(shopId, itemId) {

    alert("Accessed scrape_reviews function with Shop ID: " + shopId + " and Item ID: " + itemId);

    const reviews = [];
    const url = 'https://shopee.com.my/api/v2/item/get_ratings';
    const limit = 4;
    let offset = 0;

    const session = {
        headers: {
            'Cookie': '_gcl_au=xxxx; SPC_IA=-1; SPC_EC=-; SPC_F=xxxx; SPC_U=-; SPC_T_ID=xxxx; SPC_T_IV=xxxx; SPC_SI=xxxx; _ga=xxxx; _gid=xxxx; cto_lwid=xxxx; _fbp=xxxx; _hjid=xxxx; SPC_SIxxxx=xxxx'
        }
    };

    const fetchReviews = async () => {
        // Other code omitted for brevity
        
        if (data.error) {
            console.error(`Error: ${data.error}`);
            return reviews;
        } else if (data.data.ratings && data.data.ratings.length > 0) {
            // Display only the first review as an alert
            displayReview(data.data.ratings[0]);
            
            // Accumulate all reviews in the array if needed for further processing
            data.data.ratings.forEach((rating) => {
                const comment = rating.comment ? rating.comment.replace(/\n/g, ' ') : '';
                rating.comment = comment;
                reviews.push(rating);
            });
            offset += limit;
            return fetchReviews();
        } else {
            // Display an alert if there are no reviews
            alert("No reviews available.");
            return reviews;
        }
    };

    return fetchReviews();
}

// Function to display one review as an alert
function displayReview(review) {
    const reviewText = `Review:\n${review.author}: ${review.comment}`;
    alert(reviewText);
}

























// Function to scrape data
/* async function scrape_reviews(shopId, itemId) {

    alert("Accessed scrape_reviews function with Shop ID: " + shopId + " and Item ID: " + itemId);

    const reviews = [];
    const url = 'https://shopee.com.my/api/v2/item/get_ratings';
    const limit = 4;
    let offset = 0;

    const session = {
        headers: {
            'Cookie': '_gcl_au=xxxx; SPC_IA=-1; SPC_EC=-; SPC_F=xxxx; SPC_U=-; SPC_T_ID=xxxx; SPC_T_IV=xxxx; SPC_SI=xxxx; _ga=xxxx; _gid=xxxx; cto_lwid=xxxx; _fbp=xxxx; _hjid=xxxx; SPC_SIxxxx=xxxx'
        }
    };

    const fetchReviews = async () => {
        const params = new URLSearchParams({
            itemid: itemId,
            shopid: shopId,
            offset: offset.toString(),
            limit: limit.toString(),
            filter: '0',
            flag: '0',
            sort: '0',
            append: '0',
            before_bundle: '',
            language: 'en',
        });

        try {
            const response = await fetch(`${url}?${params.toString()}`, session);
            const data = await response.json();

            if (data.error) {
                console.error(`Error: ${data.error}`);
                return reviews;
            } else if (data.data.ratings && data.data.ratings.length > 0) {
                data.data.ratings.forEach((rating) => {
                    const comment = rating.comment ? rating.comment.replace(/\n/g, ' ') : '';
                    rating.comment = comment;
                    reviews.push(rating);
                });
                offset += limit;
                return fetchReviews();
            } else {
                return reviews;
            }
        } catch (error) {
            console.error('Error fetching data:', error);
            return reviews;
        }
    };

    return fetchReviews();
} */

/* // Function to scrape data
async function scrape_reviews(shopId, itemId) {
    const reviews = [];
    const url = 'https://shopee.com.my/api/v2/item/get_ratings';
    const limit = 4;
    let offset = 0;

    const session = {
        headers: {
            'Cookie': '_gcl_au=xxxx; SPC_IA=-1; SPC_EC=-; SPC_F=xxxx; SPC_U=-; SPC_T_ID=xxxx; SPC_T_IV=xxxx; SPC_SI=xxxx; _ga=xxxx; _gid=xxxx; cto_lwid=xxxx; _fbp=xxxx; _hjid=xxxx; SPC_SIxxxx=xxxx'
        }
    };

    const fetchReviews = async () => {
        const params = new URLSearchParams({
            itemid: itemId,
            shopid: shopId,
            offset: offset.toString(),
            limit: limit.toString(),
            filter: '0',
            flag: '0',
            sort: '0',
            append: '0',
            before_bundle: '',
            language: 'en',
        });

        try {
            const response = await fetch(`${url}?${params.toString()}`, session);
            const data = await response.json();

            if (data.error) {
                console.error(`Error: ${data.error}`);
                return reviews;
            } else if (data.data.ratings && data.data.ratings.length > 0) {
                data.data.ratings.forEach((rating) => {
                    const comment = rating.comment ? rating.comment.replace(/\n/g, ' ') : '';
                    rating.comment = comment;
                    reviews.push(rating);
                });
                offset += limit;
                return fetchReviews();
            } else {
                displayReviews(reviews); // Call displayReviews with the fetched reviews
                return reviews; // Return the accumulated reviews
            }
        } catch (error) {
            console.error('Error fetching data:', error);
            return reviews;
        }
    };

    return fetchReviews();
} */

/* // Function to display reviews as an alert
function displayReviews(reviews) {
    let reviewsText = "Reviews:\n";
    reviews.forEach((review) => {
        reviewsText += `${review.author}: ${review.comment}\n`;
    });
    alert(reviewsText);
} */

    /* // Function to display reviews in the popup
    function displayReviews(reviews) {
        const reviewsList = document.getElementById('reviewsList');
        reviewsList.innerHTML = '';
    
        reviews.forEach((review) => {
            const listItem = document.createElement('li');
            listItem.textContent = `${review.author}: ${review.comment}`;
            reviewsList.appendChild(listItem);
        });
    } */