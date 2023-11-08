function solution(skill, skill_trees) {
    let answer = 0;
    let skills = skill.split('');
    
    for(let skill_tree of skill_trees) {
        let nextSkill = 0;
        let isPossible = true;
        skill_tree = skill_tree.split('');
        for(let user_skill of skill_tree) {
            if(user_skill == skills[nextSkill]) {
                nextSkill++;
            } else if (skills.indexOf(user_skill) != -1) {
                isPossible = false;
                break;
            }
        }
        if(isPossible) answer++;
    }
    
    return answer;
}