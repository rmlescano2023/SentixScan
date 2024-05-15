let scrapeData = document.getElementById('scrapeData');

scrapeData.addEventListener("click", async () => {
    
    // Get current active tab of the chrome window
    let [tab] = await chrome.tabs.query({active: true, currentWindow: true});

    // Execute script to parse data on page
    chrome.scripting.executeScript({
        target: {tabId: tab.id},
        func: scrapeDataFromPage,
    });
})

// Function to scrape data
function scrapeDataFromPage() {
    alert('Hello world!');
}