---
title: People
permalink: /people/
---

{% assign people_sorted = site.people | sort: 'joined' %}
{% assign role_array = "faculty|phd|master|undergrade|alumni" | split: "|" %}

{% for role in role_array %}

{% assign people_in_role = people_sorted | where: 'position', role %}

<!-- Skip section if there's nobody -->
{% if people_in_role.size == 0 %}
  {% continue %}
{% endif %}

<div class="pos_header">
{% if role == 'faculty' %}
<h3>Faculty</h3>
 {% elsif role == 'phd' %}
<h3>Ph.D. Students</h3>
 {% elsif role == 'master' %}
<h3>Master Students</h3>
 {% elsif role == 'undergrade' %}
<h3>Undergraduate students</h3>
 {% elsif role == 'alumni' %}
<h3>Alumni</h3>
{% endif %}
</div>

{% if role != 'alumni' %}
<div class="content list people">
  {% for profile in people_sorted %}
    {% if profile.position contains role %}
      <div class="list-item-people">
        <p class="list-post-title">
          {% if profile.avatar %}
            <a href="{{ site.baseurl }}{{ profile.url }}"><img class="profile-thumbnail" src="{{site.baseurl}}/images/people/{{profile.avatar}}"></a>
          {% else %}
            {% if profile.gender == 'male' %}
              <a href="{{ site.baseurl }}{{ profile.url }}"><img class="profile-thumbnail" src="{{site.baseurl}}/images/people/male_avatar.png"></a>
            {% elsif profile.gender == 'female' %}
              <a href="{{ site.baseurl }}{{ profile.url }}"><img class="profile-thumbnail" src="{{site.baseurl}}/images/people/female_avatar.png"></a>
            {% else %}
              <a href="{{ site.baseurl }}{{ profile.url }}"><img class="profile-thumbnail" src="{{site.baseurl}}/images/people/default_avatar.png"></a>
            {% endif %}
          {% endif %}
          <a class="name" href="{{ site.baseurl }}{{ profile.url }}">{{ profile.name }}</a>
          {% if profile.grade %}
          <br><a class="grade">Class of {{ profile.grade }}</a>
          {% else %}
          <br><br>
          {% endif %}
        </p>
      </div>    
    {% endif %}
  {% endfor %}
</div>
<hr>

{% else %}
<br>

| Who are they | When were they here    | Where they went |
| :----------- | :--------------------- | :-------------- |
| Jiaxin Gong  | Master Students (2020) | Test            |

{% endif %}
{% endfor %}
