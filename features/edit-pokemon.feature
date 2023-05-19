Feature: Edit Pokémon
  In order to keep updated my previous registers about Pokémons
  As a user
  I want to edit a Pokémon register I created

  Background: There is a registered user and a Pokémon by one of them
    Given Exists a user "username" with password "password"
    And Exists Pokémon registered by "username"
      | nickname   | pokémon   | attack1 | attack2 | attack3 | attack4 | item        | tera-type
      | myPokemon  | bulbasaur | pound   | pound   | pound   | pound   | master-ball | normal

  Scenario: Edit owned Pokémon species
    Given I login as user "username" with password "password"
    When I edit the Pokémon with name "myPokemon"
      | species    | nickname     | attack1 | attack2 | attack3 | attack4 | item        | tera-type
      | bulbasaur   | myPokemon   | cut     | pound   | pound   | pound   | master-ball | normal
    Then I'm viewing the details for the Pokémon "myPokemon"
    And The attribute has been changed to "cut"

