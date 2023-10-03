function solution(todo_list, finished) {
    return todo_list.filter((todo, idx) => !finished[idx]);
}