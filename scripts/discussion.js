function    getUserInfo()
{
    $.getJSON("/current_user", function (data) {
        console.log(data);
        template = '<div class="username"> <span>username</span> | <span>name</span>, <span>lastname</span></div><p></p>';
        template = template.replace('username', data['username']);
        template = template.replace('name', data['name']);
        template = template.replace('lastname', data['lastname']);
        console.log(template);
        $("#userInfo").append(template);
        getAchievements(data);
        //getSpecialities(data);
    });

}