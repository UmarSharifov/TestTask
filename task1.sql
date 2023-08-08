select * from article act
  where not exists (select * from comment where article_id = act.id)