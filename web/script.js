function inputChanged(event) {
    fetch('/quersumme?n=' + event.target.value )
        .then(response => response.json())
        .then(data => {
            document.getElementById("quersumme").value = data["quersumme"];
        });
}





