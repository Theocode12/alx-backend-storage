-- a SQL script that lists all bands with Glam rock as their main style
-- ranked by their longevity
select band_name, split - formed as yr from metal_bands where style LIKE '%Glam rock%';
