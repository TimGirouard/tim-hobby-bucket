#include <jni.h>

static void

enigine_update_frame(struct engine* engine)

{
        if (engine->touchIsDown)
        {
                if (engine->touchX < 0.15f && engine->touchY < 0.2f)
                {
                        engine->playerX -= 0.015f;
                        if (engine->playerX < PADDLE_LEFT_BOUND)
                        {
                                engine->playerX = PADDLE_LEFT_BOUND;
                        }
                }
                else if (engine->touchX > 0.85f && engine->touchY < 0.2f)
                {
                        engine->playerX += 0.015f;
                        if (engine->playerX > PADDLE_RIGHT_BOUND)
                        {
                                engine->playerX = PADDLE_RIGHT_BOUND;
                        }
                }
        }

        engine->ballX += engine->ballVelocityX;
        if (engine->ballX < BALL_LEFT_BOUND || engine->ballX > BALL_RIGHT_BOUND)
        {
                engine->ballVelocityX = -engine->ballVelocityX;
        }

        engine->ballY += engine->ballVelocityY;
        if (engine->ballY > BALL_TOP_BOUND)
        {
                engine->ballVelocityY = -engine->ballVelocityY;
        }

        if (engine->ballY < BALL_BOTTOM_BOUND)
        {
                // reset the ball
                if (engine->ballVelocityY < 0.0f)
                {
                        engine->ballVelocityY = -engine->ballVelocityY;
                }

                engine->ballX = BALL_START_X;
                engine->ballY = BALL_START_Y;

                engine_init_blocks(engine);
        }

        float ballXPlusVelocity = engine->ballX + engine->ballVelocityX;
        float ballYPlusVelocity = engine->ballY + engine->ballVelocityY;

        const float ballLeft = ballXPlusVelocity - BALL_HALF_WIDTH;
        const float ballRight = ballXPlusVelocity + BALL_HALF_WIDTH;
        const float ballTop = ballYPlusVelocity + BALL_HALF_HEIGHT;
        const float ballBottom = ballYPlusVelocity - BALL_HALF_HEIGHT;
        const float paddleLeft = engine->playerX - PADDLE_HALF_WIDTH;
        const float paddleRight = engine->playerX + PADDLE_HALF_WIDTH;
        const float paddleTop = engine->playerY + PADDLE_HALF_HEIGHT;
        const float paddleBottom = engine->playerY - PADDLE_HALF_HEIGHT;
        if (!((ballRight < paddleLeft) ||
                        (ballLeft > paddleRight) ||
                        (ballBottom > paddleTop) ||
                        (ballTop < paddleBottom)))
        {
                if (engine->ballVelocityY < 0.0f)
                {
                        engine->ballVelocityY = -engine->ballVelocityY;
                }
        }
 )
        bool anyBlockActive = false;
        for (int32_t i=0; i<NUM_BLOCKS; ++i)
        {
                block& currentBlock = engine->blocks[i];
                if (currentBlock.isActive)
                {
                        const float blockLeft = currentBlock.x - BLOCK_HALF_WIDTH;
                        const float blockRight = currentBlock.x + BLOCK_HALF_WIDTH;
                        const float blockTop = currentBlock.y + BLOCK_HALF_HEIGHT;
                        const float blockBottom = currentBlock.y - BLOCK_HALF_HEIGHT;
                        if (!((ballRight < blockLeft) ||
                                        (ballLeft > blockRight) ||
                                        (ballTop < blockBottom) ||
                                        (ballBottom > blockTop)))
                        {
                                engine->ballVelocityY = -engine->ballVelocityY;

                                if (ballLeft < blockLeft ||
                                                ballRight > blockRight)
                                {
                                        engine->ballVelocityX = -engine->ballVelocityX;
                                }

                                currentBlock.isActive = false;
                        }
                        anyBlockActive = true;
                }
        }

        if (!anyBlockActive)
        {
                engine_init_blocks(engine);
        }
}
)
