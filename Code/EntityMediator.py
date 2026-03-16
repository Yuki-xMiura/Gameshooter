from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Enemy import Enemy
from code.Player import Player
from code.PlayerShot import PlayerShot
from code.Paraments import ENTITY_SCORE, LARGURA, ENTITY_DAMAGE
class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, (Enemy, EnemyShot)):
            if ent.rect.right <= 0:
                ent.health = 0 
        if isinstance(ent, (PlayerShot, EnemyShot)):
            if ent.rect.right < 0 or ent.rect.left > LARGURA:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1: Entity, ent2: Entity):
        valid_interaction = False
        if isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True
        elif isinstance(ent1, Enemy) and isinstance(ent2, Player):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True

        if valid_interaction == True:
            if ent1.rect.right >= ent2.rect.left and ent1.rect.left <= ent2.rect.right and ent1.rect.bottom >= ent2.rect.top and ent1.rect.top <= ent2.rect.bottom:
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                if ent1.health <= 0:
                    ent1.last_damage = ent2.name
                if ent2.health <= 0:
                    ent2.last_damage = ent1.name


    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_damage == 'Player1Shot':
            for ent in entity_list:
                if isinstance(ent, Player) and ent.name == 'Player1':
                    ent.score += ENTITY_SCORE[enemy.name]
            

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list[:]:  # Create a copy of the list to avoid modifying while iterating
          if ent.health <= 0:
              if isinstance(ent, Enemy):
                  EntityMediator.__give_score(ent, entity_list)
              entity_list.remove(ent)