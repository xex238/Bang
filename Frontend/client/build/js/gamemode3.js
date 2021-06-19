/******/ (function (modules) {
  // webpackBootstrap
  /******/ // The module cache
  /******/ var installedModules = {};
  /******/
  /******/ // The require function
  /******/ function __webpack_require__(moduleId) {
    /******/
    /******/ // Check if module is in cache
    /******/ if (installedModules[moduleId])
      /******/ return installedModules[moduleId].exports;
    /******/
    /******/ // Create a new module (and put it into the cache)
    /******/ var module = (installedModules[moduleId] = {
      /******/ exports: {},
      /******/ id: moduleId,
      /******/ loaded: false,
      /******/
    });
    /******/
    /******/ // Execute the module function
    /******/ modules[moduleId].call(
      module.exports,
      module,
      module.exports,
      __webpack_require__
    );
    /******/
    /******/ // Flag the module as loaded
    /******/ module.loaded = true;
    /******/
    /******/ // Return the exports of the module
    /******/ return module.exports;
    /******/
  }
  /******/
  /******/
  /******/ // expose the modules object (__webpack_modules__)
  /******/ __webpack_require__.m = modules;
  /******/
  /******/ // expose the module cache
  /******/ __webpack_require__.c = installedModules;
  /******/
  /******/ // __webpack_public_path__
  /******/ __webpack_require__.p = "";
  /******/
  /******/ // Load entry module and return exports
  /******/ return __webpack_require__(0);
  /******/
})(
  /************************************************************************/
  /******/ [
    /* 0 */
    /***/ function (module, exports, __webpack_require__) {
      var Game = __webpack_require__(2);
      var Player = __webpack_require__(4);
      var Dice = __webpack_require__(1);
      var Hint = __webpack_require__(6);
      var GameState = __webpack_require__(5);
      var View = __webpack_require__(7);

      var hint = new Hint();
      var players = new Array(6);
      for (var i = 0; i < players.length; i++) {
        players[i] = new Player("Player " + (i + 1));
      }
      var characterMaxHealthValues = true;
      var game = new Game(new Dice(), players, characterMaxHealthValues);
      game.setup();
      var gameState = new GameState(game);
      game = gameState.load();
      console.log("Active game:", game);
      var view = new View(gameState, game);
      view.hint = hint;

      window.onload = function () {
        view.grabElements();
        view.setup();
      };

      /***/
    },
    /* 1 */
    /***/ function (module, exports) {
      var Dice = function (previousObject) {
        this.currentRoll = [];
        this.saved = [];
        this.all = [];
        this.arrowsRolled = 0;
        this.rolls = 3;
        //// INFO ABOUT ABOVE:
        //// this.currentRoll - the result of the dice from the player's last roll
        //// this.saved - the dice that the player will not re-roll
        //// this.all - an array that is the same as the dice that are being displayed in the browser. It is made of the dice the player didnt re-roll and the remaining dice after they have been rolled. ( this.saved + this.currentRoll after new numbers have been generated)  Used for event listener so can use index position. the dice that are being displayed in the browser come from looping through 2 arrays(saved and currentRoll- so that saved dice wont spin) so dont have proper index positions without this.all

        this.meaningOf = {
          1: "Shoot 1",
          2: "Shoot 2",
          3: "Beer",
          4: "Gatling",
          5: "Dynamite",
          6: "Arrow",
        };

        this.imageUrl = {
          1: "../Main_bang/Bang_1.jpg",
          2: "../Main_bang/Winchester.jpg",
          3: "../Main_bang/Beer.jpg",
          4: "../Main_bang/Gatling.jpg",
          5: "../Main_bang/Dynamite.jpg",
          6: "../Main_bang/Indians.jpg",
        };

        if (previousObject !== undefined) {
          this.rehydrate(previousObject);
        }
      };

      Dice.prototype.rehydrate = function (previousObject) {
        this.currentRoll = previousObject.currentRoll;
        this.saved = previousObject.saved;
        this.all = previousObject.all;
        // this.arrowsRolled = previousObject.arrowsRolled;
        this.rolls = previousObject.rolls;
        return this;
      };

      //// Will need to reset the dice between change of player turn - use reset below.
      Dice.prototype.reset = function () {
        this.currentRoll = [];
        this.saved = [];
        this.all = [];
        this.arrowsRolled = 0;
        this.rolls = 3;
      };

      Dice.prototype.roll = function () {
        this.arrowsRolled = 0;
        if (this.canRoll() === false) return;
        this.currentRoll = [];
        var numberOfDiceToRoll = 5 - this.saved.length;

        for (var i = 0; i < numberOfDiceToRoll; i++) {
          var result = Math.floor(Math.random() * 6) + 1;
          this.currentRoll.push(result);
        }
        // console.log("Dice rolled:", this.currentRoll);

        this.saveDynamite();

        this.all = this.saved.concat(this.currentRoll);

        this.countArrows();
        this.rolls--;
        return this.currentRoll;
      };

      //// for special cards could add in above: if( playerSpecialAbility != [the special ability that lets you re-roll dynamite]){ this.saveDynamite } so save dynamite happens to everyone except the player with the special card. but it wont know what player - so would have to pass in the player object - dice.save( 0, player1) seems a bit ugly but would allow us to check player special card.

      Dice.prototype.countArrows = function () {
        for (var i = 0; i < this.currentRoll.length; i++) {
          if (this.currentRoll[i] === 6) {
            this.arrowsRolled++;
          }
        }
      };

      Dice.prototype.save = function (value) {
        if (this.saved.length < 5) this.saved.push(value);
      };
      Dice.prototype.saveDynamite = function () {
        var i = this.currentRoll.length - 1;
        for (i; i >= 0; i--) {
          if (this.currentRoll[i] === 5)
            this.save(this.currentRoll.splice(i, 1)[0]);
          // console.log("save dyna - saved:", this.saved, " current:", this.currentRoll);
        }
      };
      Dice.prototype.threeDynamite = function () {
        var counter = 0;
        for (var i = 0; i < this.all.length; i++) {
          if (this.all[i] === 5) counter++;
        }
        return counter >= 3;
      };
      Dice.prototype.canRoll = function () {
        if (this.rolls === 0) return false;
        if (this.saved.length === 5) return false;
        if (this.threeDynamite()) return false;
        return true;
      };

      //// Could possibly add in counter for each result/outcome of dice (from this.currentRoll) so that we have a total record of each thing rolled by a player that we can then send to database and we'd have stats of what each player did during game for 'review of game page' at end.

      module.exports = Dice;

      /***/
    },
    /* 2 */
    /***/ function (module, exports, __webpack_require__) {
      var playSound = __webpack_require__(3);

      var Game = function (
        dice,
        players,
        characterBasedMaxHealth,
        previousObject,
        hydratedAllPlayers
      ) {
        this.characterBasedMaxHealth = characterBasedMaxHealth;
        this.players = players;
        if (!characterBasedMaxHealth) {
          for (var i = 0; i < this.players.length; i++) {
            this.players.maxHealth = 8;
          }
        }
        if (hydratedAllPlayers !== undefined) {
          this.allPlayers = hydratedAllPlayers;
        } else {
          this.allPlayers = [];
        }
        this.characters = [];
        this.totalArrows = 9;
        this.dice = dice;
        this.wonBy = null;
        this.gatlingAvailable = true;
        if (previousObject !== undefined) {
          this.rehydrate(previousObject);
        }
        this.roles = [
          { name: "Шерифф", imgUrl: "https://i.imgur.com/yYT038yb.jpg" },
          {
            name: "Помощник Шериффа",
            imgUrl: "https://i.imgur.com/6HHgfPab.jpg",
          },

          { name: "Бандит", imgUrl: "https://i.imgur.com/NoWerAnb.jpg" },
          { name: "Бандит", imgUrl: "https://i.imgur.com/NoWerAnb.jpg" },
          { name: "Бандит", imgUrl: "https://i.imgur.com/NoWerAnb.jpg" },
          { name: "Ренегат", imgUrl: "https://i.imgur.com/TNeqBpnb.jpg" },
        ];
        var character1 = {
          name: "Джесси Джонес",
          health: 9,
          imgUrl: "../Main_bang/Jesse_Jones.jpg",
          abilityDescription:
            "Если меньше 4хп, то пиво дает +2 хп (только для себя).",
        };
        var character2 = {
          name: "Кит Карслон",
          health: 7,
          imgUrl: "../Main_bang/Kit_Carison.jpg",
          abilityDescription:
            "Обмен карт гатлинга на карты стрел (с любого игрока)",
        };
        var character3 = {
          name: "Блэк Джэк",
          health: 8,
          imgUrl: "../Main_bang/Black_Jack.jpg",
          abilityDescription: "Можно пересдавать карты динамита",
        };
        var character4 = {
          name: "Рус Дуулэн",
          health: 9,
          imgUrl: "../Main_bang/Rose_Doolan.jpg",
          abilityDescription: "Стрелковые карты имеют +1 дальность.",
        };
        var character5 = {
          name: "Педро Рамирез",
          health: 8,
          imgUrl: "../Main_bang/Pedro_Ramirez.jpg",
          abilityDescription:
            "За каждое потерянное очко здоровья, можно избавиться от одной карты стрелы.",
        };
        var character6 = {
          name: "Эль Гринго",
          health: 7,
          imgUrl: "../Main_bang/El_Gringo.jpg",
          abilityDescription:
            "За каждое потеряное вами здоровье, другой игрок берет стрелу",
        };
        var character7 = {
          name: "Барт Кэссэди",
          health: 8,
          imgUrl: "../Main_bang/Bart_Cassidy.jpg",
          abilityDescription:
            "Вы можете принять карты стрелы вместо потери здоровья (кроме случая набега индейцев или взрыва динамита).",
        };
        var character8 = {
          name: "Стервятник Сэм",
          health: 9,
          imgUrl: "../Main_bang/Vulture_Sam.jpg",
          abilityDescription: "Получаете очко здоровья за каждое убийство",
        };
        var character9 = {
          name: "Мерзкая Джанет",
          health: 8,
          imgUrl: "../Main_bang/Calamity_Janet.jpg",
          abilityDescription: "Стрелковые карты взаимозаменяемы",
        };
        var character10 = {
          name: "Человек без имени",
          health: 7,
          imgUrl: "../Main_bang/Jourdonnais.jpg",
          abilityDescription:
            "Вы можете потерять не больше 1 очка здоровья при набеге индейцев",
        };
        var character11 = {
          name: "Убийца Слэб",
          health: 8,
          imgUrl: "../Main_bang/Slab_the_Killer.jpg",
          abilityDescription:
            "Раз в ход можно удваивать стрелковые карты за счет карты пива",
        };
        var character12 = {
          name: "Сид Кэтчум",
          health: 8,
          imgUrl: "../Main_bang/Sid_Ketchum.jpg",
          abilityDescription: "В начале каждого хода даете хп любому игроку.",
        };
        var character13 = {
          name: "Сьюзи Лафаетт",
          health: 8,
          imgUrl: "../Main_bang/Suzy_Lafayette.jpg",
          abilityDescription: "Если нет стрелковых карт, то получаете хп",
        };
        var character14 = {
          name: "Пол Регрет",
          health: 9,
          imgUrl: "../Main_bang/Paul_Regret.jpg",
          abilityDescription:
            "Не теряете очки здоровья при огне Пулемета Гатлинга.",
        };
        var character15 = {
          name: "Удачливый Дюк",
          health: 8,
          imgUrl: "../Main_bang/Lucky_Duke.jpg",
          abilityDescription: "Вы имеет одну дополнительную пересдачу карт.",
        };
        var character16 = {
          name: "Малыш Вилли",
          health: 8,
          imgUrl: "../Main_bang/Willy_the_Kid.jpg",
          abilityDescription:
            "Нужно только 2 карты гатлинга чтобы открыть огонь",
        };
        this.characters = [
          character1,
          character2,
          character3,
          character4,
          character5,
          character6,
          character7,
          character8,
          character9,
          character10,
          character11,
          character12,
          character13,
          character14,
          character15,
          character16,
        ];
      };

      var getUniqueRandomElement = function (array) {
        var index = Math.floor(Math.random() * array.length);
        var choice = array[index];
        array.splice(index, 1);
        return choice;
      };

      Game.prototype.rehydrate = function (previousObject) {
        // this.characterBasedMaxHealth = previousObject.characterBasedMaxHealth;
        // if (!this.characterBasedMaxHealth){
        //   for (var i = 0; i < this.players.length; i++){
        //     this.players[i].maxHealth = 8;
        //   }
        // }
        this.totalArrows = previousObject.totalArrows;
        this.wonBy = previousObject.wonBy;
        // console.log(this.players);

        // this.allPlayers = originalOrderPlayers;
      };

      Game.prototype.setup = function () {
        this.assignRoles();
        this.assignCharacters();
        this.setAllHealth();
        this.savePlayers();
        this.rotateSheriffToFirst();
      };

      Game.prototype.rotateSheriffToFirst = function () {
        var sheriffIndex;
        for (var i = 0; i < this.players.length; i++) {
          if (this.players[i].role.name === "Шерифф") {
            sheriffIndex = i;
          }
        }
        this.rotatePlayers(sheriffIndex);
      };

      Game.prototype.setAllHealth = function () {
        for (var i = 0; i < this.players.length; i++) {
          this.players[i].setHealth();
        }
      };

      Game.prototype.assignRoles = function () {
        for (var i = 0; i < this.players.length; i++) {
          this.players[i].role = getUniqueRandomElement(this.roles);
        }
      };

      Game.prototype.assignCharacters = function () {
        for (var i = 0; i < this.players.length; i++) {
          this.players[i].character = getUniqueRandomElement(this.characters);
        } //loop
      };

      Game.prototype.savePlayers = function () {
        if (this.players.length === 6) {
          this.allPlayers = this.players.slice();
        }
      };

      Game.prototype.rotatePlayers = function (numSteps) {
        // rotates the array the number of times that is passed as an argument
        // if no argument is passed, the OR operator will set loops to 1 as numSteps will be undefined, which is falsey
        var loops = numSteps;

        if (numSteps === undefined) {
          loops = 1;
        }
        // ^ this could have been written:
        // - which might be better - passing 0 in deliberately would cause the loops to be set to 1, not 0, when using the OR operator method above - but there's no need to ever rotate the players array 0 times
        // if (numSteps === undefined){
        //   var loops = 1;
        // }
        // else{
        //   var loops = numSteps;
        // };

        for (var i = 0; i < loops; i++) {
          //2nd array item becomes first - first becomes last:
          this.players.push(this.players.shift());
          // alternative to rotate the other way:
          // last array item becomes first - first becomes 2nd:
          // this.players.unshift(this.players.pop());
        }
      };

      Game.prototype.nextTurn = function (currentPlayerDead, gameState) {
        this.checkForDeaths();
        //reset health to max in case of overhealing
        for (var i = 0; i < this.players.length; i++) {
          if (this.players[i].health > this.players[i].maxHealth) {
            this.players[i].health = this.players[i].maxHealth;
          }
        }

        var rotateSteps;
        if (currentPlayerDead === undefined || currentPlayerDead === false) {
          rotateSteps = 1;
        } else {
          rotateSteps = 0;
        }
        this.dice.reset();
        this.gatlingAvailable = true;

        this.rotatePlayers(rotateSteps);
        for (var i = 0; i < this.players.length; i++) {
          this.players[i].target = null;
        }
      };
      Game.prototype.end = function (winCheckResult) {
        Materialize.toast(winCheckResult, 3000);
        window.alert(winCheckResult);
      };
      // checks if any players have 0 health - and call the game.removePlayer(player) function on them if so
      Game.prototype.checkForDeaths = function () {
        for (var i = 0; i < this.players.length; i++) {
          if (this.players[i].health <= 0) {
            // removes target from active player if their target is dead - prevents healing your target back to 1 hp straight after you kill them, for example.
            if (this.players[i] === this.players[0].target) {
              this.players[0].target = null;
            }
            this.removePlayer(this.players[i]);
          } // "if health is 0" conditional [end]
        } // for loop [end]
        if (this.winCheck()) {
          this.end(this.winCheck());
        }
        return this.players;
      };

      Game.prototype.removePlayer = function (player) {
        this.players.splice(this.players.indexOf(player), 1);
        return this.players;
      };

      Game.prototype.winCheckOutlaws = function () {
        // console.log("outlaw wincheck  checking if array empty - players array length:", this.players.length);
        if (this.players.length === 0) {
          // console.log("game.players.length is 0 - therefore winCheckOutlaws is returning an Outlaw victory");
          return "Бандиты победили!";
        }
        // console.log("loops through players array:", this.players, "length:", this.players.length);
        for (var i = 0; i < this.players.length; i++) {
          // console.log("index:", i, "role:", this.players[i].role.name);
          if (this.players[i].role.name === "Шерифф") {
            // console.log("index:", i, "role found:", this.players[i].role.name);
            // console.log("sheriff found, returning null from outlaw wincheck");
            return null;
          }
        }
        // console.log("returning outlaws win because no sheriff found ??");
        return "Бандиты победили!";
      }; // winConditionOutlaw [end]

      Game.prototype.winCheckSheriff = function () {
        var sheriffLives = false;
        var outlawsDead = true;
        var renegadesDead = true;
        for (var i = 0; i < this.players.length; i++) {
          if (this.players[i].role.name === "Шерифф") {
            var sheriffLives = true;
          } else if (this.players[i].role.name === "Бандит") {
            outlawsDead = false;
          } else if (this.players[i].role.name === "Ренегат") {
            renegadesDead = false;
          }
        } // loop end
        if (sheriffLives && outlawsDead && renegadesDead) {
          return "Шерифф победил!";
        } else {
          return null;
        }
      };

      Game.prototype.winCheckRenegade = function () {
        if (
          this.players.length === 1 &&
          this.players[0].role.name === "Ренегат"
        ) {
          return "Ренегат победил!";
        } else {
          return null;
        }
      };

      Game.prototype.winCheck = function () {
        //all win conditions checked in appropriate order

        // the if else if statement for renegade and outlaw is important, as if the sheriff is dead, the winCheckOutlaws function returns and outlaws win - this is often correct - but if a single renegade is alive, and just killed the sheriff - then the renegade wins - so we have to check if the renegade should win first, before reverting to checking if outlaws should win in the far more common case that the renegade is not the only player left alive.

        if (this.winCheckSheriff()) {
          this.wonBy = "Шерифф";
          return this.winCheckSheriff();
        }

        var outlawCheckResult = this.winCheckOutlaws();
        var renegadeCheckResult = this.winCheckRenegade();

        if (renegadeCheckResult) {
          this.wonBy = "Ренегат";
          return renegadeCheckResult;
        } else if (outlawCheckResult) {
          this.wonBy = "Бандит";
          return outlawCheckResult;
        }
        return null;
      };

      Game.prototype.resolveArrows = function () {
        // this.assignArrows();
        for (var i = 0; i < this.dice.arrowsRolled; i++) {
          // console.log("arrows rolled", this.dice.arrowsRolled);
          //uncomment these to test currentPlayerDead behaviour MUCH more easily (refresh til no arrows on first role with sheriff, (or else outlaws win) then roll til you get one with other players to kill them straight away)
          // this.players[0].health = 1
          // this.totalArrows = 1
          this.players[0].arrows += 1;
          this.totalArrows -= 1;
          // throw new Error("giving an arrow")
          // console.log("you got an arrow");
          this.arrowsDamage();
          this.dice.arrowsRolled = 0;
        }
      };

      Game.prototype.assignArrows = function () {}; // assignArrows = function [end]

      Game.prototype.arrowsDamage = function () {
        if (this.totalArrows > 0) return null;
        this.removeHealthAndArrows();
        this.totalArrows = 9;
        Materialize.toast("Индейцы атакуют!!", 2000);
        playSound("bow-and-arrows.mp3");
        // console.log("arrows in!");
        //adding this.checkForDeaths() call  to update who can be targetted by shots still to be resolved after arrows kill some player(s), preventing them from being targetted
        this.checkForDeaths();
      }; // arrowsDamage = function [end]

      Game.prototype.removeHealthAndArrows = function () {
        for (var i = 0; i < this.players.length; i++) {
          this.players[i].health -= this.players[i].arrows;
          this.players[i].arrows = 0;
        }
      };

      Game.prototype.addToActionCounters = function () {
        this.players[0].actionCounters = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0 };
        for (var i in this.dice.all) {
          this.players[0].actionCounters[this.dice.all[i].toString()] += 1;
        }
      };

      Game.prototype.canHeal = function () {
        if (this.players[0].actionCounters["3"] > 0 && this.players[0].target) {
          return true;
        } else {
          return false;
        }
      };

      Game.prototype.canShoot = function (distance) {
        if (
          this.players[0].actionCounters[distance.toString()] > 0 &&
          (this.players[0].target === this.players[distance] ||
            this.players[0].target ===
              this.players[this.players.length - distance])
        ) {
          return true;
        } else {
          return false;
        }
      }; // canShoot = function [end]

      Game.prototype.canShoot1 = function () {
        if (
          this.players[0].actionCounters["1"] > 0 &&
          (this.players[0].target === this.players[1] ||
            this.players[0].target === this.players[this.players.length - 1])
        ) {
          return true;
        } else {
          return false;
        }
      };

      Game.prototype.canShoot2 = function () {
        if (
          this.players[0].actionCounters["2"] > 0 &&
          (this.players[0].target === this.players[2] ||
            this.players[0].target === this.players[this.players.length - 2])
        ) {
          return true;
        } else if (
          this.players[0].actionCounters["2"] > 0 &&
          this.players.length === 2 &&
          this.players[0].target === this.players[1]
        ) {
          return true;
        } else {
          return false;
        }
      };

      // ridiculous one line function body (unused) - just for fun:
      Game.prototype.canShootTargetCheck = function () {
        return (
          (this.players[0].actionCounters["1"] > 0 &&
            (this.players[0].target === this.players[1] ||
              this.players[0].target ===
                this.players[this.players.length - 1])) ||
          (this.players[0].actionCounters["2"] > 0 &&
            (this.players[0].target === this.players[2] ||
              this.players[0].target === this.players[this.players.length - 2]))
        );
      };
      // returns true if active player can shoot their current targeted player, and false if they cannot

      Game.prototype.fireGatling = function () {
        $;
        if (this.gatlingCheck()) {
          for (var i = 1; i < this.players.length; i++) {
            this.players[i].health -= 1;
          }
          this.totalArrows += this.players[0].arrows;
          this.players[0].arrows = 0;
          this.gatlingAvailable = false;
          return true;
        } else {
          return false;
        }
      };

      Game.prototype.gatlingCheck = function () {
        var counter = 0;
        for (item of this.dice.all) {
          if (item === 4) counter++;
        }
        return (
          counter >= 3 &&
          this.gatlingAvailable === true &&
          this.checkActions() <= 0
        );
      };

      Game.prototype.shootTarget = function () {
        var counterToDecrement;

        if (this.players[0].actionCounters["1"] > 0 && this.canShoot1()) {
          counterToDecrement = 1;
        } else if (
          this.players[0].actionCounters["2"] > 0 &&
          this.canShoot2()
        ) {
          counterToDecrement = 2;
        }

        if (this.players[0].target) {
          this.players[0].target.health -= 1;
          // console.log(this.players[0].name + " shot " + this.players[0].target.name)
          this.players[0].actionCounters[counterToDecrement.toString()] -= 1;
          // this.checkForDeaths();// need to update the live array if someone dies so that 1s and 2s are still accurate in terms of distance in the same turn as someone dies
        } else {
          // console.log("this is a bug - called shoot function but the button to do that should have been disabled!")
        }

        this.checkForDeaths();

        // console.log("action counters:", this.players[0].actionCounters)
      };

      Game.prototype.beerTarget = function () {
        if (this.players[0].target) {
          this.players[0].target.health += 1;

          this.players[0].actionCounters["3"] -= 1;
          // console.log(this.players[0].name + " beer'd " + this.players[0].target.name)
        } else {
          // console.log("you don't have a target to beer! how did you even click the heal button?")
        }
      };

      Game.prototype.checkActions = function () {
        var counter = 0;
        for (var i = 1; i < 4; i++) {
          if (this.players[0].actionCounters[i.toString()] > 0) {
            counter += this.players[0].actionCounters[i.toString()];
          }
        }
        return counter;
      };

      Game.prototype.dynamiteExplodes = function () {
        if (this.dice.threeDynamite()) {
          this.players[0].health -= 1;
          return true;
        }
      };

      module.exports = Game;
      module.exports.randomElement = getUniqueRandomElement;

      /***/
    },
    /* 3 */
    /***/ function (module, exports) {
      var playSound = function (sound) {
        var audio = new Audio(sound);
        audio.play();
      };

      module.exports = playSound;

      /***/
    },
    /* 4 */
    /***/ function (module, exports) {
      var Player = function (name, previousObject) {
        this.name = name || "";
        this.character = null;
        //player role is set in game model by function 'assign roles' & player character is set in game model by 'assign character'.
        this.role = null;
        this.arrows = 0;
        this.health = null;
        this.maxHealth = null;
        this.target = null;
        this.actionCounters = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0 };
        if (previousObject !== undefined) {
          this.rehydrate(previousObject);
        }
      };

      Player.prototype.rehydrate = function (previousObject) {
        this.name = previousObject.name;
        this.character = previousObject.character;
        //player role is set in game model by function 'assign roles' & player character is set in game model by 'assign character'.
        this.role = previousObject.role;
        this.arrows = previousObject.arrows;
        this.health = previousObject.health;
        this.maxHealth = previousObject.maxHealth;
        this.target = previousObject.target;
        this.actionCounters = previousObject.actionCounters;
        return this;
      };

      /// add method for player health as a percentage.
      /// add guard to stop health going below 0.

      // setHealth: run after characters and roles assigned in game model- sets health and max health from value on character card + 2 extra if sheriff.
      Player.prototype.setHealth = function () {
        this.maxHealth = this.character.health;
        if (this.role.name === "Шерифф") {
          this.maxHealth += 2;
        }
        this.health = this.maxHealth;
      };

      Player.prototype.healthDifference = function () {
        return this.maxHealth - this.health;
      };

      Player.prototype.addName = function (name) {
        this.name = name;
      };

      Player.prototype.healthAsPercentage = function () {
        return (this.health / this.maxHealth) * 100;
      };

      Player.prototype.healthAsPercentageDisplay = function () {
        var insert = this.healthAsPercentage();
        return "width: " + insert + "%";
      };

      module.exports = Player;

      /***/
    },
    /* 5 */
    /***/ function (module, exports, __webpack_require__) {
      var Player = __webpack_require__(4);
      var Game = __webpack_require__(2);
      var Dice = __webpack_require__(1);

      var GameState = function (game) {
        this.gamePassedIn = game;
        this.savedGame = null;
        this.forceNew = false;
        this.game = null;
      }; // constructor [end]

      GameState.prototype.save = function () {
        localStorage.setItem(
          "bang_the_JS_game_save",
          JSON.stringify(this.game)
        );
        console.log("Game saved:", this.game);
      };

      GameState.prototype.load = function () {
        var loadReturn = JSON.parse(
          localStorage.getItem("bang_the_JS_game_save")
        );
        this.savedGame = loadReturn;
        console.log("Saved game retrieved:", loadReturn);

        if (!this.savedGame || this.savedGame.wonBy || this.forceNew) {
          this.game = this.gamePassedIn;
          return this.gamePassedIn;
        }

        if (this.savedGame && !this.savedGame.wonBy && !this.forceNew) {
          console.log("Unfinished game loaded - preparing objects.");

          var hydratedDice = new Dice(this.savedGame.dice);
          var hydratedPlayers = new Array();
          var hydratedAllPlayers = new Array();

          for (var i = 0; i < this.savedGame.allPlayers.length; i++) {
            hydratedAllPlayers.push(
              new Player("dummy name", this.savedGame.allPlayers[i])
            );
          }

          for (var i = 0; i < hydratedAllPlayers.length; i++) {
            for (var j = 0; j < this.savedGame.players.length; j++) {
              if (
                hydratedAllPlayers[i].name === this.savedGame.players[j].name
              ) {
                hydratedPlayers[j] = hydratedAllPlayers[i].rehydrate(
                  this.savedGame.players[j]
                );
              }
            }
          }
          this.game = new Game(
            hydratedDice,
            hydratedPlayers,
            this.savedGame.characterMaxHealthValues,
            this.savedGame,
            hydratedAllPlayers
          );
          return this.game;
        } // if we want to use saved game - if statement end
      };

      module.exports = GameState;

      /***/
    },
    /* 6 */
    /***/ function (module, exports) {
      var Hint = function () {
        this.all = [
          "<b>Совет</b>: Убей чтобы победить!",
          "<b>Совет</b>: Остерегайся мерзкую Джанет.",
          "<b>Совет</b>: Используйте способности своего персонажа чтобы победить!",
          "<b>Совет</b>: Урон от стрел проходит только во время атаки Индейцев!.",
          "<b>Совет</b>: Ренегат выиграет если он убьет Шерифа оставшись 1 на 1",
          "<b>Совет</b>: Динамит нельзя пересдать.",
          "<b>Совет</b>: Стрелы нужно разрешать в конце каждого хода.",
          "<b>Совет</b>: Пулемет Гатлинга отнимает 1 хп у каждого, кроме стрелка.",
          "<b>Совет</b>: При достижении 0 хп игрок умирает.",
          "<b>Совет</b>: Если все умрут в один момент то победят бандиты!",
          "<b>Совет</b>: Помощники должны спасти Шериффа!.",
          "<b>Совет</b>: При получении 3 карт динамита вы теряете 1 хп",
          "<b>Совет</b>: Бандиты должны убить шериффа.",
          "<b>Совет</b>: Шерифф должен убить бандитов и ренегатов.",
          "<b>Совет</b>: Вы можете умереть, но ваши товарищи могут добиться победы!",
          "<b>Совет</b>: Если остался 1 Шерифф и 2 ренегата, то убив Шериффа оба ренегата проиграют (бандиты победят)",
          "<b>Совет</b>: Выберите карту которую вы хотите сохранить до пересдачи",
          "<b>Совет</b>: Если вам не нравятся карты то сделайте пересдачу.",
          "<b>Совет</b>: Шерифф всегда начинает первый.",
          "<b>Совет</b>: Нажмите на панель персонажа чтобы узнать его уникальные способности.",
        ];
      };

      module.exports = Hint;

      /***/
    },
    /* 7 */
    /***/ function (module, exports, __webpack_require__) {
      var playSound = __webpack_require__(3);

      var View = function (gameState, game) {
        this.ele = {};
        this.gameState = gameState;
        this.game = game;
        this.hint;
      }; // View constructor end

      // GET HTML ELEMENTS FROM PAGE
      View.prototype.grabElements = function () {
        // BUTTONS
        this.ele.rollDiceButton = document.getElementById("roll-dice-button");
        this.ele.healButton = document.getElementById("heal-button");
        this.ele.shootButton = document.getElementById("shoot-button");
        this.ele.endTurnButton = document.getElementById("end-turn-button");
        this.ele.roleButton = document.getElementById("role-button");
        this.ele.newGameButton = document.getElementById("new-game-button");

        // DICE IMAGES
        var dice1 = document.getElementById("dice-1");
        var dice2 = document.getElementById("dice-2");
        var dice3 = document.getElementById("dice-3");
        var dice4 = document.getElementById("dice-4");
        var dice5 = document.getElementById("dice-5");
        this.ele.dice = [dice1, dice2, dice3, dice4, dice5];

        // PLAYER LIST COMPONENT PARTS
        this.ele.playerList = [];
        var determinates = document.getElementsByClassName("determinate");
        for (var i = 1; i <= 6; i++) {
          var playerListObject = {};
          playerListObject.div = document.getElementById("player-" + i);
          playerListObject.name = document.getElementById(
            "player-" + i + "-name"
          );
          playerListObject.avatar = document.getElementById(
            "player-" + i + "-avatar"
          );
          playerListObject.character = document.getElementById(
            "player-" + i + "-character"
          );
          playerListObject.healthBar = document.getElementById(
            "player-" + i + "-health-bar"
          );
          playerListObject.healthDiv = document.getElementById(
            "player-" + i + "-health-div"
          );
          playerListObject.currentPlayerDiv = document.getElementById(
            "player-" + i + "-cp-div"
          );
          playerListObject.currentPlayerText = document.getElementById(
            "current-player-" + i
          );
          playerListObject.sheriffIcon = document.querySelector(
            "li.player-" + i + ", i.sheriff-icon"
          );

          // playerListObject.healthBarFill = determinates[i-1];
          // console.log("player"+i+"healthBar: ", playerListObject.healthBar);
          // console.log("player"+i+"healthBarFill: ", playerListObject.healthBarFill);

          this.ele.playerList.push(playerListObject);
        } // for loop 8 [end]
        // console.log(this.ele.playerList[0].healthBarFill);
        var allHealthBars = document.getElementsByClassName("determinate");
        // console.log(allHealthBars);
        // console.log(allHealthBars.length);
        // CURRENT PLAYER
        // this.ele.currentPlayer = document.getElementById('current-player');
        this.ele.currentPlayerAvatar = document.getElementById(
          "current-player-avatar"
        );
        this.ele.currentPlayerAvatarReveal = document.getElementById(
          "current-player-avatar-reveal"
        );
        this.ele.currentPlayerNameRole = document.getElementById(
          "current-player-name-character"
        );
        this.ele.currentPlayerCharacter = document.getElementById(
          "current-player-character"
        );
        this.ele.currentPlayerAbility = document.getElementById(
          "current-player-ability"
        );
        this.ele.currentPlayerHealth = document.getElementById(
          "current-player-health"
        );
        this.ele.currentPlayerArrows = [];
        for (var i = 1; i <= 9; i++) {
          this.ele.currentPlayerArrows.push(
            document.getElementById("current-player-arrow-" + i)
          );
        }
        // TARGET ARROW PILE PICTURES
        this.ele.arrowPile = [];
        for (var i = 1; i <= 9; i++) {
          this.ele.arrowPile.push(document.getElementById("arrow-" + i));
        }
        // TARGET HINT CARD
        this.ele.hintElement = document.getElementById("hint");
      }; // grabElements method [end]
      View.prototype.updateHealthBars = function () {
        for (i = 0; i < this.game.allPlayers.length; i++) {
          this.ele.playerList[i].healthBar.style.width =
            this.game.allPlayers[i].healthAsPercentage() + "%";
          this.game.checkForDeaths();
        }
      }; // updateHealthBars = function [end]
      View.prototype.renderPlayerListItem = function (playerIndex) {
        var playerObject = this.ele.playerList[playerIndex];
        // var playerItem = this.ele.playerListItems[playerIndex];
        playerObject.name.setAttribute(
          "class",
          "title grey-text text-darken-4"
        );
        playerObject.name.innerHTML =
          "<b>" + this.game.allPlayers[playerIndex].name + "</b>";
        playerObject.character.setAttribute("class", "grey-text text-darken-4");
        playerObject.currentPlayerDiv.style.display = "none";
        playerObject.healthDiv.style.display = "block";
        playerObject.healthDiv.setAttribute("class", "progress red lighten-4");
        playerObject.div.setAttribute("class", "collection-item avatar player");
        playerObject.healthBar.style.display = "block"; // IMPORTANT - some bars default to display: none - some default to block
        playerObject.healthBar.style.width =
          this.game.allPlayers[playerIndex].healthAsPercentage() + "%";

        if (this.game.allPlayers[playerIndex] == this.game.players[0]) {
          playerObject.currentPlayerText.innerText = "Current Player";
          playerObject.name.setAttribute("class", "title white-text");
          playerObject.character.setAttribute("class", "white-text");
          playerObject.healthDiv.style.display = "none";
          playerObject.currentPlayerDiv.style.display = "inline-block";
          playerObject.currentPlayerDiv.setAttribute(
            "class",
            "grey-text text-lighten-4"
          );
          playerObject.currentPlayerDiv.innerHTML =
            '<b id="current-player-5">Current Player</b>';
          playerObject.div.setAttribute(
            "class",
            "collection-item avatar red darken-4 player"
          );
        } else if (this.game.allPlayers[playerIndex] == this.game.players[1]) {
          playerObject.name.innerHTML =
            "<b>" + this.game.allPlayers[playerIndex].name + "</b>" + " - NEXT";
        } else if (
          this.game.allPlayers[playerIndex] ==
          this.game.players[this.game.players.length - 1]
        ) {
          playerObject.name.innerHTML =
            "<b>" +
            this.game.allPlayers[playerIndex].name +
            "</b>" +
            " - PREVIOUS";
        } else {
          playerObject.name.innerHTML =
            "<b>" + this.game.allPlayers[playerIndex].name + "</b>";
        }
        if (this.game.allPlayers[playerIndex].role.name === "Sheriff") {
          playerObject.avatar.src =
            this.game.allPlayers[playerIndex].role.imgUrl;
          playerObject.character.innerText =
            this.game.allPlayers[playerIndex].role.name;
        } else {
          playerObject.avatar.src =
            this.game.allPlayers[playerIndex].character.imgUrl;
          playerObject.character.innerText =
            this.game.allPlayers[playerIndex].character.name;
        }
        if (this.game.allPlayers[playerIndex].health <= 0) {
          playerObject.character.innerText =
            this.game.allPlayers[playerIndex].role.name;
          playerObject.avatar.src =
            this.game.allPlayers[playerIndex].role.imgUrl;
          playerObject.div.setAttribute(
            "class",
            "collection-item avatar grey lighten-4 player"
          );
          playerObject.div.onclick = null;
          playerObject.currentPlayerText.setAttribute(
            "class",
            "grey-text text-darken-4"
          );
          playerObject.currentPlayerText.innerText = "DEAD";

          playerObject.currentPlayerDiv.style.display = "inline";
          playerObject.healthDiv.style.display = "none";
          playerObject.character.innerHTML =
            this.game.allPlayers[playerIndex].role.name;
          playerObject.avatar.src =
            this.game.allPlayers[playerIndex].role.imgUrl;
          // sets text colour to black for "DEAD" text:
          playerObject.currentPlayerDiv.setAttribute(
            "class",
            "grey-text text-darken-4"
          );
          //possibly unnecessary?:
          playerObject.currentPlayerDiv.style.display = "inline";
          playerObject.healthBar.style.display = "none";
        }
      }; // renderPlayerListItem = function [end]
      // // old view healthbars function
      // var updateHealthBars = function(){
      //   for(i = 0; i < allHealthBars.length; i++){
      //     allHealthBars[i].style.width = game.allPlayers[i].healthAsPercentage() + "%";
      //     playerObject.determinate
      //     var p = document.getElementById("player-" + (i + 1));
      //     playerObject.div
      //     var pChar = document.getElementById("player-" + (i + 1) + "-character");
      //     playerObject.character
      //     var pAva = document.getElementById("player-" + (i + 1) + "-avatar");
      //     playerObject.avatar
      //     var pDead = document.getElementById("current-player-" + (i + 1));
      //     playerObject.currentPlayerText
      //     var pDeadDiv = document.getElementById("player-" + (i + 1) + "-cp-div");
      //     playerObject.currentPlayerDiv
      //     var pHealthBar = document.getElementById("player-" + (i + 1) + "-health-div");
      //     playerObject.healthDiv
      //     if(game.allPlayers[i].health <= 0){
      //       game.checkForDeaths();
      //       p.onclick = null;
      //       p.setAttribute('class', 'collection-item avatar grey lighten-4 player');
      //       pChar.innerHTML = game.allPlayers[i].role.name;
      //       pAva.src = game.allPlayers[i].role.imgUrl;
      //       pDead.innerText = 'DEAD';
      //       pDead.setAttribute('class', 'grey-text text-darken-4')
      //       pDeadDiv.style.display = "inline";
      //       pHealthBar.style.display = "none";
      //     }
      //   }
      // }
      View.prototype.setup = function () {
        this.setNewGameButtonOnClick();

        this.renderCurrentPlayer();
        this.renderPlayerList();
        this.renderHintCard();
        this.renderArrowPile();

        this.renderDice(null);
        this.setAllDiceOnClicks(null);

        this.setHealButtonOnClick(null);
        this.setShootButtonOnClick(null);
        this.setEndTurnButtonOnClick(null);
        this.setViewRoleButtonOnClick();
        this.setRollDiceButtonOnClick();
        this.setPlayerListOnClicks();
      }; // setup = function [end]
      View.prototype.renderUpdateAll = function () {
        this.renderCurrentPlayer();
        this.renderPlayerList();
        this.renderHintCard();
        this.renderArrowPile();
        this.renderDice();
      }; // renderUpdateAll = function [end]
      // ON CLICK EVENTS SETTERS ////////////////////////////////////////////////////
      View.prototype.setNewGameButtonOnClick = function (remove) {
        if (remove === null) {
          this.ele.newGameButton.onclick = null;
          return;
        }
        this.ele.newGameButton.onclick = function () {
          this.gameState.forceNew = true;
          this.game = this.gameState.load();
          this.gameState.forceNew = false;
          this.setup();
        }.bind(this);
      }; // setNewGameButtonOnClick = function [end]
      View.prototype.setRollDiceButtonOnClick = function (remove) {
        if (remove === null) {
          this.ele.rollDiceButton.onclick = null;
          this.ele.rollDiceButton.setAttribute(
            "class",
            "waves-effect waves-light btn disabled"
          );
          return;
        }
        this.ele.rollDiceButton.setAttribute(
          "class",
          "waves-effect waves-light btn red darken-4"
        );
        this.ele.rollDiceButton.onclick = function () {
          this.rollDice();
          this.renderDice();
          this.setAllDiceOnClicks();
          this.game.resolveArrows();
          this.renderCurrentPlayerHealth();
          this.renderCurrentPlayerArrows();
          this.enableShootButton();
          this.currentPlayerDied();
          this.game.checkForDeaths();
          this.enableShootButton();
          this.renderCurrentPlayerHealth();
          this.updateHealthBars();
          if (this.game.dice.canRoll() === false) {
            //maybe re-add duplicate "use all dice to end turn" toast
            this.setRollDiceButtonOnClick(null);
            this.game.addToActionCounters();
          }
          this.diceRollFinished();
        }.bind(this);
      }; // setRollDiceButtonOnClick = function [end]

      View.prototype.setAllDiceOnClicks = function (remove) {
        if (remove === null) {
          for (var i = 0; i < 5; i++) {
            this.setDiceOnClick(i, null);
          }
          return;
        }
        // console.log(this.game.dice.saved.length);
        for (var i = this.game.dice.saved.length; i < 5; i++) {
          this.setDiceOnClick(i);
        }
      }; // setAllDiceOnClicks = function [end]

      View.prototype.setDiceOnClick = function (diceNumber, remove) {
        if (remove === null) {
          this.ele.dice[diceNumber].onclick = null;
          // this.ele.dice[diceNumber].style.opacity = 0.5;
          // console.log("SETDICEONCLICK called with null args");
          // throw new Error("setDiceOnClick null call - trace")
          // CALLED ON NEXT TURN
          return;
        }
        this.ele.dice[diceNumber].style.opacity = 1;
        this.ele.dice[diceNumber].onclick = function () {
          var diceValue = this.game.dice.all[diceNumber];
          if (diceValue !== 5) this.game.dice.save(diceValue);
          this.ele.dice[diceNumber].style.opacity = 0.5;
          this.ele.dice[diceNumber].onclick = null;
          this.diceRollFinished();
        }.bind(this);
        // console.log(this.ele.dice[diceNumber]);
        // console.log(this.ele.dice[diceNumber].onclick);
      }; // setDiceOnClick = function [end]

      // //////////////////////////////////////////////////
      // checking / doing stuff functions  // //////////////////////////////////////////////////
      // //////////////////////////////////////////////////

      View.prototype.ifCurrentPlayerDead = function () {
        // console.log(this.game)
        this.game.nextTurn(true, this.gameState);
        this.gameState.save(); // save state of the game at another time without resetting dice and rotating players and in theory we could possibly continue the turn with the dice and rerolls remembered
        // updateDisplayForNewTurn function here (grey out and remove onclicks for dead players - reset buttons etc.)
        this.setup();
        this.renderDice(null);
        this.currentPlayerDied(); // checks again after players rotated - in case player rotated to died to arrows same as the previous player
        this.setup();
        this.ele.endTurnButton.setAttribute(
          "class",
          "waves-effect waves-light btn disabled"
        );
      }; // currentPlayerDeadBehaviour = function [end]
      View.prototype.currentPlayerDied = function () {
        if (this.game.players[0].health > 0) return false;
        this.renderCurrentPlayerHealth();
        this.renderCurrentPlayerArrows();
        this.setRollDiceButtonOnClick(null);
        this.setEndTurnButtonOnClick(null);
        setTimeout(this.ifCurrentPlayerDead, 3000); // function definition just above
        return true;
      }; // currentPlayerDied = function [end]
      View.prototype.rollDice = function () {
        this.game.dice.roll();
        this.renderDice();

        this.game.resolveArrows();
        this.renderPlayerList();
        this.renderCurrentPlayerArrows();
        this.renderCurrentPlayerHealth();
        this.currentPlayerDied();
        this.enableShootButton();
        this.renderArrowPile();
        this.renderCurrentPlayerArrows(); // in case current player dies - shows their new arrows (probably 0, cause arrows just went back to the middle)
        this.renderCurrentPlayerHealth(); // in case current players dies - shows their 0 filled hearts
        this.updateHealthBars();

        this.currentPlayerDied();
        this.renderCurrentPlayerArrows(); // NECESSARY duplication
        this.renderCurrentPlayerHealth(); // NECESSARY duplication
        this.updateHealthBars();
        this.game.checkForDeaths();

        if (this.game.dice.threeDynamite()) {
          this.dynamiteExplodes();
        }

        this.currentPlayerDied();
        this.renderCurrentPlayerArrows(); // NECESSARY duplication
        this.renderCurrentPlayerHealth(); // NECESSARY duplication
        this.updateHealthBars();
      }; // rollDice = function [end]
      View.prototype.dynamiteExplodes = function () {
        this.game.dynamiteExplodes();
        playSound("audio/dynamite.mp3");
        Materialize.toast("Boom!", 2000);
      }; // dynamiteExplodes = function [end]
      View.prototype.enableShootButton = function () {
        //have to .bind(this) to keep this scoped to the view object - 'this' scope becomes Window without binding
        var shootEnableFunctions = {
          1: this.enableShootButtonOnePlayer.bind(this),
          2: this.enableShootButtonTwoPlayers.bind(this),
          3: this.enableShootButtonThreePlayers.bind(this),
          4: this.enableShootButtonFourPlayers.bind(this),
        };
        var numPlayers = this.game.players.length;
        if (numPlayers > 4) numPlayers = 4;
        var appropriateFunction = shootEnableFunctions[numPlayers];
        appropriateFunction();
      }; // enableShootButton = function [end]

      View.prototype.setViewRoleButtonOnClick = function (remove) {
        if (remove === null) {
          this.ele.roleButton.setAttribute(
            "class",
            "waves-effect waves-light btn disabled"
          );
          this.ele.roleButton.onclick = null;
          return;
        }
        this.ele.roleButton.onclick = function () {
          this.setViewRoleButtonOnClick(null);
          Materialize.toast(
            "For your eyes only...",
            2000,
            "",
            function () {
              this.ele.currentPlayerAvatarReveal.src =
                this.game.players[0].role.imgUrl;
              this.ele.currentPlayerCharacter.innerHTML =
                this.game.players[0].role.name +
                '<i class="material-icons right">close</i>';

              setTimeout(
                function () {
                  this.ele.currentPlayerAvatarReveal.src =
                    this.game.players[0].character.imgUrl;
                  this.ele.currentPlayerCharacter.innerHTML =
                    this.game.players[0].character.name +
                    '<i class="material-icons right">close</i>';
                  this.ele.roleButton.setAttribute(
                    "class",
                    "btn waves-effect waves-light red darken-4"
                  );
                  this.setViewRoleButtonOnClick();
                }.bind(this),
                1500
              );
            }.bind(this)
          );
        }.bind(this);
      }; // setViewRoleButtonOnClick = function [end]
      View.prototype.setEndTurnButtonOnClick = function (remove) {
        this.fireGatling();
        this.ele.endTurnButton.setAttribute(
          "class",
          "waves-effect waves-light btn red darken-4"
        );
        if (this.game.fireGatling()) {
          playSound("audio/gatling-gun.mp3");
          this.updateHealthBars();
        }
        if (remove === null) {
          this.ele.endTurnButton.setAttribute(
            "class",
            "waves-effect waves-light btn disabled"
          );
          this.ele.endTurnButton.onclick = null;
        }
        this.ele.endTurnButton.onclick = function () {
          this.game.nextTurn(false, this.gameState);
          this.gameState.save(); // save state of the game at another time without resetting dice and rotating players and in theory we could possibly continue the turn with the dice and rerolls remembered
          this.setup();
          this.ele.endTurnButton.setAttribute(
            "class",
            "waves-effect waves-light btn disabled"
          );
          this.setRollDiceButtonOnClick();
        }.bind(this);
      }; // setEndTurnButtonOnClick = function [end]

      View.prototype.setPlayerListOnClicks = function () {
        for (var i = 0; i < this.game.allPlayers.length; i++) {
          this.setPlayerListItemOnClick(i);
        }
      }; // setPlayerListOnClicks = function [end]
      View.prototype.setPlayerListItemOnClick = function (playerIndex) {
        this.ele.playerList[playerIndex].div.onclick = function () {
          if (
            this.game.players[0].target === this.game.allPlayers[playerIndex]
          ) {
            this.game.players[0].target = null;
          } else {
            this.game.players[0].target = this.game.allPlayers[playerIndex];
          }
          this.targetPlayer(this.ele.playerList[playerIndex].div);
          this.enableShootButton();

          this.game.canHeal()
            ? this.setHealButtonOnClick()
            : this.setHealButtonOnClick(null);
        }.bind(this);
      }; // setPlayerListItemOnClick = function [end]
      View.prototype.targetPlayer = function (selectedDiv) {
        var healthBar = selectedDiv.getElementsByClassName("progress")[0];
        // TARGET PREVIOUSLY SELECTED PLAYER
        var previouslySelected =
          document.getElementsByClassName(
            "collection-item avatar player red lighten-4"
          )[0] ||
          document.getElementsByClassName(
            "collection-item grey darken-3 avatar player"
          )[0];
        // TARGET HEALTH BAR OF PREVIOUSLY SELECTED PLAYER
        if (previouslySelected)
          var targetedHealthBar =
            previouslySelected.getElementsByClassName("progress")[0];

        // RESET PREVIOUSLY SELECTED PLAYER COLOURS
        if (previouslySelected && previouslySelected != selectedDiv) {
          if (
            previouslySelected.className ===
            "collection-item grey darken-3 avatar player"
          ) {
            previouslySelected.setAttribute(
              "class",
              "collection-item avatar red darken-4 player"
            );
          } else {
            previouslySelected.setAttribute(
              "class",
              "collection-item avatar player"
            );
            targetedHealthBar.setAttribute("class", "progress red lighten-4");
          }
        }

        // IF SELECTED PLAYER IS CURRENTLY UNSELECTED, SELECT THEM
        if (selectedDiv.className === "collection-item avatar player") {
          selectedDiv.setAttribute(
            "class",
            "collection-item avatar player red lighten-4"
          );
          healthBar.setAttribute("class", "progress white");

          // IF SELECTED PLAYER IS RED, MAKE THEM BLACK
        } else if (
          selectedDiv.className === "collection-item avatar red darken-4 player"
        ) {
          selectedDiv.setAttribute(
            "class",
            "collection-item grey darken-3 avatar player"
          );
          // IF SELECTED PLAYER IS BLACK, MAKE THEM RED
        } else if (
          selectedDiv.className ===
          "collection-item grey darken-3 avatar player"
        ) {
          selectedDiv.setAttribute(
            "class",
            "collection-item avatar red darken-4 player"
          );
          // IF SELECTED PLAYER IS CURRENTLY SELECTED, DESELECT THEM
        } else {
          selectedDiv.setAttribute("class", "collection-item avatar player");
          healthBar.setAttribute("class", "progress red lighten-4");
        }
      }; // targetPlayer = function [end]
      // UNUSED
      View.prototype.endGame = function () {
        // TRIGGER END GAME MODAL
        // DISABLE BUTTONS
        // removes targets from all players to allow saving without JSON.stringify throwing a "gameState.js:12 Uncaught TypeError: Converting circular structure to JSON"
        // (can't save a player object with a player object nested in it - definitely not if it's the SAME player object (if targetting yourself and turn end-)
        // see also: https://github.com/isaacs/json-stringify-safe/blob/master/README.md
        for (var i = 0; i < this.players.length; i++) {
          this.players[i].target = null;
        }
        // console.log("saving finished game");
        view.gameState.save();
        view.game.end();
      }; // endGame = function [end]
      View.prototype.setShootButtonOnClick = function (remove) {
        if (remove === null) {
          this.ele.shootButton.setAttribute(
            "class",
            "waves-effect waves-light btn disabled"
          );
          this.ele.shootButton.onclick = null;
          return;
        }
        this.ele.shootButton.setAttribute(
          "class",
          "waves-effect waves-light btn red darken-4"
        );
        this.ele.shootButton.onclick = function () {
          if (this.game.players[0].target.health < 2) {
            var shootMessage = "You killed " + this.game.players[0].target.name;
          } else {
            var shootMessage = "You shot " + this.game.players[0].target.name;
          }
          Materialize.toast(shootMessage, 2000);
          this.game.shootTarget();
          playSound("audio/pistol-riccochet.ogg");
          // this line was causing inverted target highlighting:
          // this.renderPlayerList();

          if (this.game.canShoot1()) {
            this.setShootButtonOnClick();
          } else if (!this.game.canShoot1() && !this.game.canShoot2()) {
            this.setShootButtonOnClick(null);
          }
          if (this.game.canShoot2()) {
            this.setShootButtonOnClick();
          } else if (!this.game.canShoot2() && !this.game.canShoot1()) {
            this.setShootButtonOnClick(null);
          }

          this.game.canShoot1() || this.game.canShoot2()
            ? this.setShootButtonOnClick()
            : this.setShootButtonOnClick(null);
          if (this.game.canHeal()) {
            this.setHealButtonOnClick();
          } else {
            this.setHealButtonOnClick(null);
          }

          this.updateHealthBars();
          if (this.game.checkActions() <= 0) {
            this.setEndTurnButtonOnClick();
          }
        }.bind(this); // onclick end
      }; // setShootButtonOnClick = function [end]
      View.prototype.setHealButtonOnClick = function (remove) {
        if (remove === null) {
          this.ele.healButton.setAttribute(
            "class",
            "waves-effect waves-light btn disabled"
          );
          this.ele.healButton.onclick = null;
          return;
        }
        this.ele.healButton.setAttribute(
          "class",
          "waves-effect waves-light btn red darken-4"
        );
        this.ele.healButton.onclick = function () {
          Materialize.toast(
            "You healed " + this.game.players[0].target.name,
            2000
          );
          playSound("audio/bottle-pour.mp3");
          this.game.beerTarget();
          if (this.game.canHeal()) {
            this.setHealButtonOnClick();
          } else {
            this.setHealButtonOnClick(null);
          }
          this.updateHealthBars();
          this.renderCurrentPlayerHealth();
          if (this.game.checkActions() <= 0) {
            this.setEndTurnButtonOnClick();
          }
        }.bind(this);
      }; // setHealButtonOnClick = function [end]
      View.prototype.enableShootButtonFourPlayers = function () {
        if (this.game.canShoot1()) {
          this.setShootButtonOnClick();
          playSound("audio/shotgun-cock.wav");
        } else if (!this.game.canShoot1() && !this.game.canShoot2()) {
          this.setShootButtonOnClick(null);
        }
        if (this.game.canShoot2()) {
          this.setShootButtonOnClick();
          playSound("audio/revolver-cock.wav");
        } else if (!this.game.canShoot2() && !this.game.canShoot1()) {
          this.setShootButtonOnClick(null);
        }
      }; // enableShootButtonFourPlayers = function [end]
      View.prototype.enableShootButtonThreePlayers = function () {
        if (this.game.canShoot1() && this.game.canShoot2()) {
          this.setShootButtonOnClick();
          playSound("audio/shotgun-cock.wav");
        } else if (this.game.canShoot1()) {
          this.setShootButtonOnClick();
          playSound("audio/shotgun-cock.wav");
        } else if (!this.game.canShoot1() && !this.game.canShoot2()) {
          this.setShootButtonOnClick(null);
        }
      }; // enableShootButtonThreePlayers = function [end]
      View.prototype.enableShootButtonTwoPlayers = function () {
        if (
          this.game.players[0].target == this.game.players[1] &&
          this.game.players[0].actionCounters["1"]
        ) {
          this.setShootButtonOnClick();
          playSound("audio/shotgun-cock.wav");
        } else if (
          this.game.players[0].target == this.game.players[1] &&
          this.game.players[0].actionCounters["2"]
        ) {
          this.setShootButtonOnClick();
          playSound("audio/revolver-cock.wav");
        } else if (this.game.players[0].target == this.game.players[0]) {
          // console.log("You can't shoot yourself, try shooting the other surviving player");
          this.setShootButtonOnClick(null);
        }
      }; // enableShootButtonTwoPlayers = function [end]
      View.prototype.enableShootButtonOnePlayer = function () {
        if (
          this.game.players[0].target == this.game.players[0] &&
          (this.game.players[0].actionCounters["1"] ||
            this.game.players[0].actionCounters["2"])
        ) {
          // console.log("You can't shoot yourself - the game should be over, you're the only player alive");
          this.setShootButtonOnClick(null);
        }
      }; // enableShootButtonOnePlayer = function [end]
      View.prototype.enableHealButton = function () {
        if (this.game.canHeal()) {
          this.setHealButtonOnClick();
        } else {
          this.setHealButtonOnClick(null);
        }
      }; // enableHealButton = function [end]
      View.prototype.fireGatling = function () {
        if (this.game.gatlingCheck()) {
          this.game.fireGatling();
          Materialize.toast(this.game.players[0].name + " Used gatling!", 2000);
          playSound("audio/gatling-gun.mp3");
          this.updateHealthBars();
          this.game.checkForDeaths();
        }
      }; // fireGatling = function [end]
      View.prototype.diceRollFinished = function () {
        if (this.game.dice.canRoll() === false) {
          this.game.addToActionCounters();
          if (this.game.checkActions()) {
            Materialize.toast(
              "Target a player to resolve dice before ending turn",
              3500
            );
            this.enableShootButton();
            //added shootButtonEnable check here so that if targeting a player, then saving all dice, you can shoot that target straight away without reselecting them
          }
          for (var i = 0; i < this.ele.dice.length; i++)
            this.ele.dice[i].style.opacity = 1;
          this.game.addToActionCounters();
          this.ele.rollDiceButton.setAttribute(
            "class",
            "waves-effect waves-light btn disabled"
          );
          this.ele.rollDiceButton.onclick = null;
          if (this.game.checkActions() <= 0) {
            this.fireGatling();
            this.setEndTurnButtonOnClick();
            this.ele.rollDiceButton.setAttribute(
              "class",
              "waves-effect waves-light btn disabled"
            );
          }
        }
      };
      // //////////////////////////////////////////////////// //////////////////////////////////////////////////
      // RENDER METHODS // //////////////////////////////////////////////////
      // //////////////////////////////////////////////////// //////////////////////////////////////////////////
      View.prototype.renderDice = function (remove) {
        if (remove === null) {
          for (var i = 0; i < this.ele.dice.length; i++) {
            this.ele.dice[i].style.visibility = "hidden";
            this.ele.dice[i].src = null;
            this.ele.dice[i].onclick = null;
            // console.log("RENDERDICE called with null arg");
            // NOT CALLED ON END TURN
          }
        }
        var diceCount = 0;
        for (diceCount; diceCount < this.game.dice.saved.length; diceCount++) {
          this.ele.dice[diceCount].src =
            this.game.dice.imageUrl[this.game.dice.saved[diceCount]];
          this.ele.dice[diceCount].onclick = null;
          this.ele.dice[diceCount].style.opacity = 0.5;
          this.ele.dice[diceCount].style.visibility = "visible";
        }
        // DISPLAY CURRENT ROLL
        var totalDice = this.game.dice.currentRoll.length + diceCount;
        for (diceCount; diceCount < totalDice; diceCount++) {
          this.ele.dice[diceCount].src =
            this.game.dice.imageUrl[this.game.dice.all[diceCount]];
          this.ele.dice[diceCount].style.visibility = "visible";
          this.ele.dice[diceCount].style.opacity = 1;
        }
        if (this.game.dice.saved.length === 5) {
          for (var i = 0; i < this.game.dice.all; i++) {
            this.ele.dice[diceCount].style.opacity = 1;
          }
        }
      }; // renderDice = function [end]
      View.prototype.renderArrowPile = function () {
        for (var i = 0; i < this.ele.arrowPile.length; i++) {
          this.ele.arrowPile[i].src = "http://i.imgur.com/pUn7Uru.png";
          this.ele.arrowPile[i].style.visibility = "visible";
          if (i >= this.game.totalArrows)
            this.ele.arrowPile[i].style.visibility = "hidden";
        } // loop [end]
      }; // renderArrowPile = function [end]
      View.prototype.renderCurrentPlayer = function () {
        this.ele.currentPlayerAvatar.src =
          this.game.players[0].character.imgUrl;
        this.ele.currentPlayerAvatarReveal.src =
          this.game.players[0].character.imgUrl;
        this.ele.currentPlayerNameRole.innerHTML =
          "<b>" +
          this.game.players[0].name +
          "</b> - " +
          this.game.players[0].character.name;
        this.ele.currentPlayerCharacter.innerHTML =
          this.game.players[0].character.name +
          '<i class="material-icons right">close</i>';
        this.ele.currentPlayerAbility.innerText =
          this.game.players[0].character.abilityDescription;

        this.renderCurrentPlayerHealth();
        this.renderCurrentPlayerArrows();
      }; // renderCurrentPlayer = function [end]
      View.prototype.renderCurrentPlayerHealth = function () {
        this.ele.currentPlayerHealth.innerHTML = "";
        var overhealed = false;
        if (this.game.players[0].health > this.game.players[0].maxHealth)
          overhealed = true;
        // console.log("overhealed: ", overhealed);
        var numHeartsToDraw = this.game.players[0].health;
        // console.log("HP before overhealed check:", this.game.players[0].health);
        // console.log("MAX HP before overhealed check:", this.game.players[0].maxHealth);
        if (overhealed === true) {
          numHeartsToDraw = this.game.players[0].maxHealth;
        }
        // console.log("overhealed boolean:",overhealed, "health to draw:", numHeartsToDraw);
        for (var i = 0; i < numHeartsToDraw; i++) {
          this.ele.currentPlayerHealth.innerHTML +=
            '<i class="material-icons hp-icon">favorite</i>';
        }
        for (var i = 0; i < this.game.players[0].healthDifference(); i++) {
          this.ele.currentPlayerHealth.innerHTML +=
            '<i class="material-icons hp-icon">favorite_outline</i>';
        }
      }; // renderCurrentPlayerHealth = function [end]
      View.prototype.renderCurrentPlayerArrows = function () {
        for (var i = 0; i < this.ele.currentPlayerArrows.length; i++) {
          this.ele.currentPlayerArrows[i].src =
            "https://i.imgur.com/e6hASp9.png";
          this.ele.currentPlayerArrows[i].style.display = "inline-block";
          if (i >= this.game.players[0].arrows)
            this.ele.currentPlayerArrows[i].style.display = "none";
        }
      }; // renderCurrentPlayerArrows = function [end]
      View.prototype.renderPlayerList = function () {
        for (var i = 0; i < this.game.allPlayers.length; i++) {
          this.renderPlayerListItem(i);
        }
        // this.updateHealthBars(); // doesn't fix new game health bar display bug
      }; // renderPlayerList = function [end]
      View.prototype.renderHintCard = function () {
        // HINT CARD
        this.ele.hintElement.innerHTML =
          this.hint.all[Math.floor(Math.random() * this.hint.all.length)];
      }; // renderHintCard = function [end]

      module.exports = View;

      /***/
    },
    /******/
  ]
);
//# sourceMappingURL=bundle.js.map
