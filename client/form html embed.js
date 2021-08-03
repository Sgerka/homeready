// JS
// on button click
document.querySelector('.copy-text').addEventListener('click', () => {
    // paste your function - start
    var text = $('#myInput').text();
    navigator.clipboard.writeText(text).then(function () {
        console.log('Async: Copying to clipboard was successful!');
    }, function (err) {
        console.error('Async: Could not copy text: ', err);
    });
    // paste your function - end
});
