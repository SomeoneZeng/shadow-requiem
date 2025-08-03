class_name Player extends CharacterBody2D

var gravity := ProjectSettings.get("physics/2d/default_gravity") as float
var move_speed : float = 100.0


#func _process(delta: float) -> void:
	#
	#var direction : Vector2 = Vector2.ZERO
	#direction.x = Input.get_action_strength("right") - Input.get_action_strength("left")
	#direction.y = Input.get_action_strength("down") - Input.get_action_strength("up")
	#
	#velocity = direction * move_speed
	#
	#pass

func _physics_process(delta: float) -> void:
	print("Delta time: ", delta)
	velocity.y += gravity * delta
	move_and_slide()
