/* https://leetcode.com/problems/not-boring-movies/submissions/ */

SELECT * FROM cinema
WHERE (id % 2 != 0) AND description != "boring";
ORDER BY rating DESC;