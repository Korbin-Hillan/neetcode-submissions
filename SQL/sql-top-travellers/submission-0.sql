-- Write your query below
SELECT u.name, COALESCE(SUM(r.distance), 0) AS travelled_distance
FROM USERS u
LEFT JOIN RIDES r ON ( u.id = r.user_id )
GROUP BY u.id,u.name
ORDER BY travelled_distance DESC, u.name ASC;