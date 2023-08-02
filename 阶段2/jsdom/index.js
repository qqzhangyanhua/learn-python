const jsdom = require('jsdom')
const { JSDOM } = jsdom

const resourceLoader = new jsdom.ResourceLoader({
    userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
})
const html = `<!DOCTYPE html><p>hello</p>`
const dom = new JSDOM(html, {
    url: 'https://www.haizol.com/',
    referrer: 'https://baidu.com/',
    contentType: 'text/html',
    includeNodeLocations: true,
    storageQuota: 10000000,
    runScripts: 'dangerously',
    resources: resourceLoader,
})
console.log('dom.window.document', dom.window.document)
console.log('dom.window.document.body', dom.window.document.body)