
CREATE TABLE `game` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `status` varchar(30) DEFAULT 'open',
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `sequence` varchar(100) NOT NULL,
  `creator` varchar(30) NOT NULL DEFAULT 'anonymous',
  `step` int(11) NOT NULL DEFAULT '0'
);


CREATE TABLE `player` (
  `id` varchar(30) NOT NULL,
  `avatar` varchar(100) NOT NULL DEFAULT 'anonymous',
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ;


CREATE TABLE `playergame` (
  `game` int(11) NOT NULL,
  `player` varchar(30) NOT NULL,
  `status` varchar(30) NOT NULL DEFAULT 'new',
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ;

ALTER TABLE `game`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `player`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `playergame`
  ADD KEY `game` (`game`),
  ADD KEY `player` (`player`);

ALTER TABLE `game`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

ALTER TABLE `playergame`
  ADD CONSTRAINT `game` FOREIGN KEY (`game`) REFERENCES `game` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `player` FOREIGN KEY (`player`) REFERENCES `player` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;