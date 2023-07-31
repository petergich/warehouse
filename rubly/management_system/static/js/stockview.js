const dateField = document.querySelector('.opening_stock');
const DateField = document.querySelector('.closing_stock');
dateField.addEventListener('change', (event) => {
    const dateVal = event.target.value;
    console.log(dateVal);
    let json = JSON.stringify({openingdate :dateVal});
    console.log(json);
    if  (dateVal.length > 0 ){
        var url = "dashboardstock/?openingdate=" + encodeURIComponent(dateVal);
        window.location.href = url;
       
}

});
DateField.addEventListener('change', (event) => {
    const dateVal = event.target.value;
    if  (dateVal.length > 0 ){
        var url = "dashboardstock/?closingdate=" + encodeURIComponent(dateVal);
        window.location.href = url;
       
}

});

