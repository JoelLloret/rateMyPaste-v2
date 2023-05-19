Feature: Register Paste
  In order to keep track of the Pastes I own
  As a user
  I want to register my personal Pastes, along with the Pokémons contained in it

  Background: There is a registered user
    Given Exists a user "username" with password "password"

  Scenario: Register new Paste
    Given I login as user "username" with password "password"
    And Exists Pokémon registered by "username"
      | nickname   | species   | attack1 | attack2 | attack3 | attack4 | item        | tera-type
      | myPokemon1 | bulbasaur | pound   | pound   | pound   | pound   | master-ball | normal
      | myPokemon2 | bulbasaur | pound   | pound   | pound   | pound   | master-ball | normal
      | myPokemon3 | bulbasaur | pound   | pound   | pound   | pound   | master-ball | normal
      | myPokemon4 | bulbasaur | pound   | pound   | pound   | pound   | master-ball | normal
      | myPokemon5 | bulbasaur | pound   | pound   | pound   | pound   | master-ball | normal
      | myPokemon6 | bulbasaur | pound   | pound   | pound   | pound   | master-ball | normal

    When I register Paste
      | name    | pokemon1    | pokemon2    | pokemon3    | pokemon4    | pokemon5    | pokemon6    | pokepaste_code
      | myPaste1 | myPokemon1  | myPokemon2  | myPokemon3  | myPokemon4  | myPokemon5  | myPokemon6 | 0000
    Then I'm viewing the list of all Pastes of "username"
      | Pastes         |
      | myPaste        |


  Scenario: Try to register Paste but not logged in
    Given I'm not logged in
    When I register Pokémon
      | nickname   | species   | attack1 | attack2 | attack3 | attack4 | item        | tera-type
      | myPokemon  | bulbasaur | pound   | pound   | pound   | pound   | master-ball | normal
    Then I'm redirected to the login form