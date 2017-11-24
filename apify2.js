// page specific scrape for summary [Medlineplus disease page]
// sample: https://medlineplus.gov/a1c.html
// returns only summary

function pageFunction(context) {
    // called on every page the crawler visits, use it to extract data from it
    var $ = context.jQuery;
    var results = []
        $("#topic-summary").each(function() {
        results.push({
            sum: $(this).find("p:first").text()
        });
    })
    return results;
}
