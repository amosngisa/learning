const taskInput = document.getElementById("task-input");
const addTaskBtn = document.getElementById("add-task-btn");
const taskList = document.getElementById("task-list");

//Adding task
addTaskBtn.addEventListener("click", function() {
  const taskText = taskInput.value;
  if (taskText.trim() !== "") {
    const taskItem = document.createElement("li");
    taskItem.innerText = taskText;

    taskList.appendChild(taskItem);
    taskInput.value = "";
  }
});

//Removing task
taskList.addEventListener("click", function(event) {
    let jibu = confirm(`Do you want to delete ${taskList.innerText}?`);

if (jibu === true){
    if (event.target.tagName.toLowerCase() === "li") {
        event.target.remove();
      }
}
else{
    alert("You canceled");
}
    
  });