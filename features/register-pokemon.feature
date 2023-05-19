Feature: Register Pokémon
  In order to keep track of the Pokémons I own
  As a user
  I want to register my personal Pokémon, along with its details (nickname, species, attacks, item and tera type)

  Background: There is a registered user
    Given Exists a user "username" with password "password"

  Scenario: Register new Pokémon
    Given I login as user "username" with password "password"
    When I register Pokémon
      | species    | nickname   | attack1 | attack2 | attack3 | attack4 | item        | tera_type
      | Bulbasaur  | myPokemon  | pound   | pound   | pound   | pound   | master-ball | normal
    Then I'm viewing the list of all Pokémons of "username"
      | nickname       |
      | myPokemon        |


  Scenario: Try to register restaurant but not logged in
    Given I'm not logged in
    When I register Pokémon
      | nickname   | species   | attack1 | attack2 | attack3 | attack4 | item        | tera-type
      | myPokemon  | bulbasaur | pound   | pound   | pound   | pound   | master-ball | normal
    Then I'm redirected to the login form