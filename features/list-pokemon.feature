Feature: List Pokémons
  In order to keep myself up to date about Pokémons I own
  As a user
  I want to list all my registered Pokémons

  Background: There are 5 registered Pokémons by same user
    Given Exists a user "username" with password "password"
    And I login as user "username" with password "password"
    And Exists Pokémon registered by "username"
      | nickname   | pokemon    | attack1 | attack2 | attack3 | attack4 | item        | tera-type
      | myPokemon1  | bulbasaur | pound   | pound   | pound   | pound   | master-ball | normal
      | myPokemon2  | bulbasaur | pound   | pound   | pound   | pound   | master-ball | normal
      | myPokemon3  | bulbasaur | pound   | pound   | pound   | pound   | master-ball | normal
      | myPokemon4  | bulbasaur | pound   | pound   | pound   | pound   | master-ball | normal
      | myPokemon5  | bulbasaur | pound   | pound   | pound   | pound   | master-ball | normal

  Scenario: List the five Pokémons
    When I list Pokémons
    Then I'm viewing a list of Pokémons containing
      | myPokemon1       | myPokemon2       | myPokemon3       | myPokemon4       | myPokemon5       |
    And The list contains 5 Pokémons