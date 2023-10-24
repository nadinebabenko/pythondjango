export class TodoList {
    constructor() {
      this.tasks = [];
    }
  
    addTask(task) {
      this.tasks.push({ task, completed: false });
    }
  
    markTaskAsComplete(index) {
      if (index >= 0 && index < this.tasks.length) {
        this.tasks[index].completed = true;
      }
    }
  
    listAllTasks() {
      this.tasks.forEach((task, index) => {
        console.log(`${index + 1}. ${task.task} - ${task.completed ? 'Completed' : 'Incomplete'}`);
      });
    }
  }