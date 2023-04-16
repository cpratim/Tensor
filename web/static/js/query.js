let dropdownBtn = document.getElementById('drop-text');
let list = document.getElementById('list');
let icon = document.getElementById('icon');
let span = document.getElementById('span');
let input = document.getElementById('search-input');
let listItems = document.querySelectorAll('.dropdown-list-item');
let submitButton = document.getElementById("button");

dropdownBtn.onclick = function() {
    if (list.classList.contains('show')) {
        icon.style.rotate = "0deg";
    }
    else {
        icon.style.rotate = "-180deg";
    }
    list.classList.toggle('show');
};

window.onclick = function(event) {
    if (
        event.target.id !== "drop-text" &&
        event.target.id !== "span" &&
        event.target.id !== "icon"
    ) {
        list.classList.remove('show');
        icon.style.rotate = "0deg";
    }
}

for (item of listItems) {
    item.onclick = function (e) {
        span.innerText = e.target.innerText;

        input.placeholder = "Search for " + e.target.innerText + "...";
    };
}

submitButton.addEventListener("click", function(event) {
    var table = document.getElementById("tbody");

    $.getJSON('/sample_query.json', function(data) {
        for (var i = 0; i < data.length; i++) {
            displayResult(data[i]);
        }
    });

    function displayResult(data) {
        var tr = document.createElement("tr");
        console.log(data);
        let length = (data[3].length * 5 / data[2].length) * 100;
        tr.innerHTML = `
        
            <td> 
            <p class="difficulty ${data[4]}"><i class='bx bxs-checkbox'></i></p>
            </td>
            <td> ${data[1]} </td>
            <td> ${data[5]} </td>
            <td> ${data[2]} </td>
            <td> ${data[3]} </td>
            <td>
                <div class="progressbar">
                    <div style="width: ${length}%"></div>
                    </div>
            </td>
        `
        table.appendChild(tr);
        
    }
});

$(submitButton).onclick(function() {
    
    
});


