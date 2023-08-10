function addBook() {
    let title = document.getElementById("title").value;
    let author = document.getElementById("author").value;
    let year = document.getElementById("year").value;

    let divBook = document.createElement("div");
    divBook.setAttribute("class", "bookItem");
    let bookItem = document.querySelector("ul");
    bookItem.append(divBook)
    
    let liItem = document.createElement("li");
    liItem.append("\"" + title +"\"" +  ", " + author + ", " + year + "r");
    divBook.append(liItem);
    

    let delBtn = document.createElement("input");
    delBtn.setAttribute("type", "button");
    delBtn.setAttribute("value", "Delete");
    delBtn.setAttribute("class", "btnItem");
    divBook.append(delBtn);
    delBtn.addEventListener("click", function() {
        let ulList = document.querySelector("#liBook");
        let delBook = document.querySelector(".bookItem");
        ulList.removeChild(delBook);
      });

}  

document.getElementById("submit").onclick = addBook;
