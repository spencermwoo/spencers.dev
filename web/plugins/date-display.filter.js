const { DateTime } = require("luxon");


function readableDate(dateObj) {
    return DateTime.fromJSDate(dateObj, {zone: 'utc'}).toFormat("dd LLL yyyy");
}

function htmlDateString(dateObj) {
    return DateTime.fromJSDate(dateObj, {zone: 'utc'}).toFormat('yyyy-LL-dd');
}

module.exports = {readableDate, htmlDateString}


// .eleventy.js
// const {readableDate, htmlDateString} = require('./configs/date-display.filter');
// eleventyConfig.addFilter('readableDate', readableDate);
// eleventyConfig.addFilter('htmlDateString', htmlDateString);