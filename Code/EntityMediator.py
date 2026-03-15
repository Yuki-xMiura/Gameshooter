from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Enemy import Enemy
from code.PlayerShot import PlayerShot
from code.Paraments import LARGURA
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
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list[:]:  # Create a copy of the list to avoid modifying while iterating
          if ent.health <= 0:
              entity_list.remove(ent)