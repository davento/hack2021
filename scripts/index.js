function searchPaper() {
    
}

function getRecommendations()
{
    getPaperInfo();
}

function getPaperInfo()
{
    $.getJSON("/", function(data) {
        console.log(data);
        template = '<div><h3><span>title</span></h3><h4>By <span>author</span></h4>Posted on: <span>date</span><p></p>Published by: <span>publisher</span></div>';
        template = template.replace('title', data['title']);
        template = template.replace('author', data['name']);
        template = template.replace('date', data['date']);
        template = template.replace('publisher', data['publisher']);
        template += '<button onclick ="paperRedirect("' + str(data['link']) + '")"></button>'
        $("#paperInfo").append(template);
    }
    )
}

function paperRedirect(url) {
    window.open(url, '_blank');
}

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