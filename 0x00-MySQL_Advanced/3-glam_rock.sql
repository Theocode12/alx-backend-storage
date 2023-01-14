-- a SQL script that lists all bands with Glam rock as their main style
-- ranked by their longevity
SELECT band_name, IFNULL(metal_bands.split, YEAR(CURDATE())) - formed AS lifespan
	FROM metal_bands 
	WHERE style LIKE '%Glam rock%';
