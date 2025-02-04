function addTask() {
    let taskInput = document.getElementById("taskInput");
    let taskText = taskInput.value.trim();
    if (!taskText) return;

    let li = document.createElement("li");
    li.className = "task-item";

    let checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.onclick = () => toggleTask(checkbox);

    let span = document.createElement("span");
    span.textContent = taskText;

    let button = document.createElement("button");
    button.className = "delete-btn";
    button.innerHTML = "🗑";
    button.onclick = () => li.remove();

    li.append(checkbox, span, button);
    document.getElementById("taskList").appendChild(li);

    taskInput.value = "";
}

function toggleTask(checkbox) {
    let taskText = checkbox.nextElementSibling;
    taskText.style.textDecoration = checkbox.checked ? "line-through" : "none";
    taskText.style.color = checkbox.checked ? "gray" : "black";
}
