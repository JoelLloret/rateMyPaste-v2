Feature: List Paste
  In order to keep myself up to date about my Pastes
  As a user
  I want to list all my created Pastes

  Background: There are 6 registered Pokémons by same user, and 3 Pastes registered by the same user
    Given Exists a user "username" with password "password"
    And I login as user "username" with password "password"
    And Exists Pokémon registered by "username"
      | nickname   | species    | attack1 | attack2 | attack3 | attack4 | item        | tera-type
      | myPokemon1  | bulbasaur | pound   | pound   | pound   | pound   | master-ball | normal
      | myPokemon2  | bulbasaur | pound   | pound   | pound   | pound   | master-ball | normal
      | myPokemon3  | bulbasaur | pound   | pound   | pound   | pound   | master-ball | normal
      | myPokemon4  | bulbasaur | pound   | pound   | pound   | pound   | master-ball | normal
      | myPokemon5  | bulbasaur | pound   | pound   | pound   | pound   | master-ball | normal
    And Exists Paste registered by "username"
      | name     | pokemon1    | pokemon2    | pokemon3    | pokemon4    | pokemon5    | pokemon6   | pokepaste_code
      | myPaste1 | myPokemon1  | myPokemon2  | myPokemon3  | myPokemon4  | myPokemon5  | myPokemon6 | 0000
      | myPaste2 | myPokemon1  | myPokemon2  | myPokemon3  | myPokemon4  | myPokemon5  | myPokemon6 | 0000
      | myPaste3 | myPokemon1  | myPokemon2  | myPokemon3  | myPokemon4  | myPokemon5  | myPokemon6 | 0000

  Scenario: List the last three
    When I list Pastes
    Then I am viewing a Paste list containing:
      | Paste          |
      | myPaste1       |
      | myPaste2       |
      | myPaste3       |