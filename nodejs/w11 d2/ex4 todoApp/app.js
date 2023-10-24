import { TodoList } from './todo.js';

const todoList = new TodoList();

todoList.addTask('Buy groceries');
todoList.addTask('Do laundry');
todoList.addTask('Clean the house');
todoList.markTaskAsComplete(1);

todoList.listAllTasks();