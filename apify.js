// https://medlineplus.gov/healthtopics_a.html
// Displays title of all links + respective websites. Limited to first 15 to prevent crashing on website during test
// TO DO: open up each URL, export first paragraph of disease summary, add to database

function pageFunction(context) {
    // called on every page the crawler visits, use it to extract data from it
    var $ = context.jQuery;
    var results = [];
    $("section a").each(function() {
        if (results.length < 15) {
            results.push({
                    title: $(this).text(),
                    link: $(this).attr('href')
            });
        }
    })
    return results;
}
