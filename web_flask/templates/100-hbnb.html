<!DOCTYPE html>
<HTML lang="en">
  <HEAD>
    <META charset="utf-8">
    <META name="viewport" content="width=device-width, initial-scale=1">
    <TITLE>HBnB</TITLE>
    <LINK rel="stylesheet" href="../static/styles/reset.css">
    <LINK rel="stylesheet" href="../static/styles/103-common.css">
    <LINK rel="stylesheet" href="../static/styles/103-header.css">
    <LINK rel="stylesheet" href="../static/styles/103-footer.css">
    <LINK rel="stylesheet" href="../static/styles/103-filters.css">
    <LINK rel="stylesheet" href="../static/styles/103-places.css">
    <LINK rel="stylesheet"
          href="https://use.fontawesome.com/releases/v5.7.2/css/all.css"
          integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr"
          crossorigin="anonymous">
    <LINK rel="icon" href="../static/images/icon.png">
  </HEAD>

  <BODY>
    <HEADER></HEADER>

    <MAIN>
      <DIV class="container">
        <SECTION class="filters" role="search">
          <DIV class="locations">
            <H3>States</H3>
            <H4>&nbsp;</H4>
            <DIV class="popover">
							<UL>
              {% for state in states.values()|sort(attribute="name") %}
                <LI><STRONG>{{ state.name }}</STRONG>
                  <UL>
                  {% for city in state.cities|sort(attribute="name") %}
                    <LI>{{ city.name }}</LI>
                  {% endfor %}
                  </UL>
                </LI>
              {% endfor %}
              </UL>
            </DIV>

            </DIV><DIV class="amenities">
              <H3>Amenities</H3>
              <H4>&nbsp;</H4>
              <UL class="popover">
                {% for amenity in amenities.values()|sort(attribute="name") %}
                  <LI>{{ amenity.name}}</LI>
                {% endfor %}
              </UL>
            </DIV>
          <BUTTON>Search</BUTTON>
        </SECTION>

        <SECTION class="places">
          <H1>Places</H1>
          {% for place in places.values()|sort(attribute="name") %}
          <ARTICLE>
            <DIV class="title_box">
              <H2>{{ place.name }}</H2>
              <DIV class="price_by_night">&#36;{{ place.price_by_night }}</DIV>
            </DIV>

            <DIV class="information">
              <DIV class="max_guest">
                <I class="fa fa-users fa-3x" aria-hidden="true"></I>
                <BR>{{ place.max_guest }} Guests
              </DIV>
              <DIV class="number_rooms">
                <I class="fa fa-bed fa-3x" aria-hidden="true"></I>
                <BR>{{ place.number_rooms }} Rooms
              </DIV>
              <DIV class="number_bathrooms">
                <I class="fa fa-bath fa-3x" aria-hidden="true"></I>
                <BR>{{ place.number_bathrooms }} Bathrooms
              </DIV>
            </DIV>

            <DIV class="user">
              <STRONG>Owner:</STRONG> {{ place.user.first_name }} {{ place.user.last_name }}
            </DIV>

            <DIV class="description">{{ place.description|safe }}</DIV>

            <DIV class="amenities">
              <H2>Amenities</H2>
              {% for amenity in place.amenities|sort(attribute="name") %}
              <UL>
                <LI><P>{{ amenity.name }}</P></LI>
              </UL>
              {% endfor %}
            </DIV>

            <DIV class="reviews">
              <H2>{{ place.reviews.__len__() }} Reviews</H2>
              {% for review in place.reviews %}
              <H3>From {{ review.user.first_name }} the {{ review.created_at.date().__str__() }}</H3>
              <UL>
                <LI><P>{{ review.text|safe }}</P></LI>
              </UL>
            {% endfor %}
            </DIV>
          </ARTICLE>
          {% endfor %}
        </SECTION>
      </DIV>
    </MAIN>

    <FOOTER>
      Holberton School
    </FOOTER>
  </BODY>
</HTML>
