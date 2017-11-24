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


