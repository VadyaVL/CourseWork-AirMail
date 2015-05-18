delimiter |
CREATE EVENT IF NOT EXISTS `DeleteInactive`
ON SCHEDULE
  EVERY 2 DAY STARTS DATE_FORMAT(NOW(), '%Y-%m-%d 03:00:00')
  DO
  BEGIN
		SET SQL_SAFE_UPDATES = 0;

		DELETE FROM airmaildb.message WHERE Dialogue_id_id IN (
		SELECT id FROM airmaildb.dialogue WHERE 
		TIMESTAMPDIFF(DAY, dialogue.Established,NOW())>2 and dialogue.CountMess<6);   

		DELETE FROM airmaildb.dialogue WHERE 
		TIMESTAMPDIFF(DAY, dialogue.Established,NOW())>2 and dialogue.CountMess<6;
	END |
delimiter ;
 
 
 
SET GLOBAL event_scheduler = ON;

USE airmaildb;
SHOW EVENTS;
DROP EVENT `DeleteInactive`;
ALTER EVENT `DeleteInactive` ENABLE;
