def study_schedule(permanence_period, target_time):
  # 1.3 - Retorne None se target_time recebe um valor vazio;
  if not target_time:
    return None

  student_quantities = 0

  for period in permanence_period:
    # 1.2 - Retorne None se em permanence_period houver alguma entrada inválida;
    if (not isinstance(period[0], int)) or (not isinstance(period[1], int)):
      return None

    if (target_time >= period[0]) and (target_time <= period[1]):
      student_quantities += 1

  # 1.1 - Retorne a quantidade de estudantes presentes para uma entrada específica;
  return student_quantities

  # 1.4 - A função deverá, por meio de análise empírica, se comportar (no avaliador remoto em sua Pull Request) como no máximo O(n), ou seja, com complexidade assintótica linear.